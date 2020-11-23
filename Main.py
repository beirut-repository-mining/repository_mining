import argparse
from projects import ProjectName, Project
from data_extractor import DataExtractor
from version_selector import VersionType
from config import Config
import os
import json
from pathlib import Path
import pandas as pd
from metrics.version_metrics import Extractor
from metrics.version_metrics_data import DataBuilder
from metrics.version_metrics_name import DataNameEnum
from classification_instance import ClassificationInstance
from itertools import tee
import time


class Main():
    def __init__(self):
        self.project = None
        self.extractor = None
        self.save_data_names()
        self.jira_url = None
        self.github_user_name = None

    def list_projects(self):
        print("\n".join(list(map(lambda e: "{0}: {1}".format(e.name, e.value.description()), ProjectName))))

    def extract(self):
        self.extractor.extract(True)

    def set_project(self, github, jira):
        self.project = Project(github.lower(), jira.upper())
        self.set_extractor()

    def set_project_enum(self, name):
        self.project = ProjectName[name].value
        self.set_extractor()

    def set_extractor(self):
        self.extractor = DataExtractor(self.project, self.jira_url, self.github_user_name)

    def extract_metrics(self, rest_versions, rest_only, data_types):
        classes_datasets = []
        methods_datasets = []
        if not rest_only:
            for version in self.extractor.get_selected_versions()[:-1]:
                classes_df, methods_df = self.extract_features_to_version(version, True, data_types)
                classes_datasets.append(classes_df)
                methods_datasets.append(methods_df)
        for version in rest_versions:
            try:
                self.extract_features_to_version(version, False, data_types)
            except:
                pass
        if rest_only:
            return
        self.predict(classes_datasets[:-1], classes_datasets[-1], methods_datasets[:-1], methods_datasets[-1])

    def predict(self, c_training, c_testing, m_training, m_testing):
        classes_instance = self.extract_classes_datasets(c_training, c_testing)
        classes_instance.predict()

        methods_instance = self.extract_methods_datasets(m_training, m_testing)
        methods_instance.predict()

    def get_data_dirs(self):
        classes_data = Config.get_work_dir_path(os.path.join(Config().config['CACHING']['RepositoryData'],
                                                             Config().config['VERSION_METRICS']['ClassesData'],
                                                             self.project.github()))
        method_data = Config.get_work_dir_path(
            os.path.join(Config().config['CACHING']['RepositoryData'], Config().config['VERSION_METRICS']['MethodData'],
                         self.project.github()))
        intermediate_dir = Config.get_work_dir_path(
            os.path.join(Config().config['CACHING']['RepositoryData'],
                         Config().config['VERSION_METRICS']['Intermediate'],
                         self.project.github()))
        classes_intermediate_dir = os.path.join(intermediate_dir, "classes")
        methods_intermediate_dir = os.path.join(intermediate_dir, "methods")
        Path(classes_intermediate_dir).mkdir(parents=True, exist_ok=True)
        Path(methods_intermediate_dir).mkdir(parents=True, exist_ok=True)
        Path(classes_data).mkdir(parents=True, exist_ok=True)
        Path(method_data).mkdir(parents=True, exist_ok=True)
        return classes_data, method_data, classes_intermediate_dir, methods_intermediate_dir, intermediate_dir

    def aggrate_methods_df(self, df):
        def clean(s):
            if "@" in s:
                return s[1].split('@')[1].split('.')[:-1][-1]
            return s[1].split('.')[:-1][-1]
        ids = df['Method_ids'].iteritems()
        files_id, classes_id = tee(ids, 2)
        files = pd.Series(list(map(lambda x: x[1].split('@')[0], files_id))).values
        classes = pd.Series(list(map(clean, classes_id))).values
        df.insert(0, 'File', files)
        df.insert(0, 'Class', classes)
        groupby = ['File', 'Class']
        columns_filter = ['File', 'Class', 'BuggedMethods', 'Method', 'Method_ids']
        columns = list(
            filter(lambda x: x not in columns_filter, df.columns.values.tolist()))
        data = list()
        for key, group in df.groupby(groupby):
            key_data = {}
            key_data.update(dict(zip(groupby, key)))
            for feature in columns:
                pt = pd.DataFrame(group[feature].describe()).T
                cols = ["{0}_{1}".format(feature, c) for c in pt.columns.values.tolist()]
                pt.columns = cols
                key_data.update(list(pt.iterrows())[0][1].to_dict())
            data.append(key_data)
        return pd.DataFrame(data)

    def fillna(self, df, default=False):
        if 'Bugged' in df:
            df = df[df['Bugged'].notna()]
        if 'BuggedMethods' in df :
            df = df[df['BuggedMethods'].notna()]
        for col in df:
            dt = df[col].dtype
            if dt == int or dt == float:
                df[col].fillna(0, inplace=True)
            else:
                df[col].fillna(default, inplace=True)
        return df

    def extract_features_to_version(self, version, extract_bugs, data_types):
        self.extractor.checkout_version(version)
        db, extractors_to_run = self.get_extractors(data_types, extract_bugs, version)
        for extractor in extractors_to_run:
            start = time.time()
            extractor.extract()
            print(time.time() - start, extractor.__class__.__name__)
        classes_df, methods_df = db.build()
        methods_df = self.fillna(methods_df)
        aggregated_methods_df = self.aggrate_methods_df(methods_df)
        if 'Class' in classes_df.columns and 'Class' in aggregated_methods_df.columns:
            classes_df = classes_df.merge(aggregated_methods_df, on=['File', 'Class'], how='outer')
        else:
            classes_df = classes_df.merge(aggregated_methods_df, on=['File'], how='outer')
        classes_df = self.fillna(classes_df)
        methods_df = methods_df.drop('File', axis=1, errors='ignore')
        methods_df = methods_df.drop('Class', axis=1, errors='ignore')
        methods_df = methods_df.drop('Method', axis=1, errors='ignore')
        self.save_dfs(classes_df, methods_df, aggregated_methods_df, version)
        return classes_df, methods_df

    def save_dfs(self, classes_df, methods_df, aggregated_methods_df, version):
        classes_data, method_data, classes_intermediate_dir, methods_intermediate_dir, intermediate_dir = self.get_data_dirs()
        classes_df.to_csv(os.path.join(classes_intermediate_dir, version + ".csv"), index=False, sep=';')
        methods_df.to_csv(os.path.join(methods_intermediate_dir, version + ".csv"), index=False, sep=';')
        aggregated_methods_df.to_csv(os.path.join(intermediate_dir, version + "aggregated_methods_df.csv"), index=False, sep=';')
        classes_df.to_csv(os.path.join(classes_data, version + ".csv"), index=False, sep=';')
        methods_df.to_csv(os.path.join(method_data, version + ".csv"), index=False, sep=';')

    def get_extractors(self, data_types, extract_bugs, version):
        db = DataBuilder(self.project, version)
        if extract_bugs:
            data_types.add("bugged")
            data_types.add("bugged_methods")
        extractors_to_run = set()
        for extractor in Extractor.get_all_extractors(self.project, version):
            if not extract_bugs and "bugged" in extractor.__class__.__name__.lower():
                continue
            extractor_data_types = []
            for dt in extractor.data_types:
                if dt.value in data_types:
                    extractor_data_types.append(dt)
                    extractors_to_run.add(extractor)
            db.add_data_types(extractor_data_types)
        return db, extractors_to_run

    def extract_classes_datasets(self, training_datasets, testing_dataset):
        training = pd.concat(training_datasets, ignore_index=True).drop(["File", "Class", "Method_ids"], axis=1, errors='ignore')
        training = self.fillna(training)
        testing = testing_dataset.drop("Method_ids", axis=1, errors='ignore')
        testing = self.fillna(testing, default='')
        file_names = testing.pop("File").values.tolist()
        classes_names = testing.pop("Class").values.tolist()
        classes_testing_names = list(map("@".join, zip(file_names, ['' if x in (False, True) else x for x in classes_names])))
        return ClassificationInstance(training, testing, classes_testing_names, self.get_dataset_dir("classes"))

    def get_dataset_dir(self, sub_dir):
        dataset_dir = Config.get_work_dir_path(
            os.path.join(Config().config['CACHING']['RepositoryData'], Config().config['VERSION_METRICS']['Dataset'],
                         self.project.github()))
        sub_dataset_dir = os.path.join(dataset_dir, sub_dir)
        Path(sub_dataset_dir).mkdir(parents=True, exist_ok=True)
        return sub_dataset_dir

    def extract_methods_datasets(self, training_datasets, testing_dataset):
        training = pd.concat(training_datasets, ignore_index=True).drop("Method_ids", axis=1, errors='ignore')
        training = self.fillna(training)
        testing = testing_dataset
        testing = self.fillna(testing)
        methods_testing_names = testing.pop("Method_ids").values.tolist()
        return ClassificationInstance(training, testing, methods_testing_names, self.get_dataset_dir("methods"), label="BuggedMethods")

    def choose_versions(self, version_num=5, algorithm="bin", version_type=VersionType.Untyped, strict=True):
        self.extractor.choose_versions(version_num=version_num, algorithm=algorithm, strict=strict, version_type=version_type)

    def set_version_selection(self, version_num=5, algorithm="bin", version_type=VersionType.Untyped, strict=True, selected_config=0):
        self.extractor.choose_versions(version_num=version_num, algorithm=algorithm, strict=strict, version_type=version_type, selected_config=selected_config)
        self.extractor.selected_config = selected_config
        assert self.extractor.get_selected_versions()

    def save_data_names(self):
        j = list()
        out_path = Config.get_work_dir_path(
            os.path.join(Config().config['CACHING']['RepositoryData'], "dataname.json"))
        for d in DataNameEnum:
            j.append(d.value.as_description_dict())
        with open(out_path, "w") as f:
            json.dump(j, f)

    def main(self):
        parser = argparse.ArgumentParser(description='Execute project data')
        parser.add_argument('-p', '--projects', dest='projects', action='store_const', const=True, default=False,
                            help='list all aleready defined projects')
        parser.add_argument('-c', '--choose', dest='choose', action='store', help='choose a project to extract')
        parser.add_argument('-g', '--github_repo_name', dest='github', action='store', help='the github repository name to the project to extract (lowercase)')
        parser.add_argument('-j', '--jira_name', dest='jira', action='store', help='the jira name to the project to extract (uppercase)')
        parser.add_argument('-u', '--github_user_name', dest='github_user_name', action='store', help='the github user name to the project to extract (lowercase)', default="apache")
        parser.add_argument('-jl', '--jira_url', dest='jira_url', action='store', help='the link to jira', default="http://issues.apache.org/jira")
        parser.add_argument('-l', '--list_select_verions', dest='list_selected', action='store', help='the algorithm to select the versions : [bin]', default='bin')
        parser.add_argument('-d', '--data_types_to_extract', dest='data_types', action='store', help='Json file of the data types to extract as features. Choose a sublist of '
                                                                                                    '[checkstyle, designite_design, designite_implementation, '
                                                                                                    'designite_type_organic, designite_method_organic, designite_type_metrics,'
                                                                                                    'designite_method_metrics, source_monitor_files, source_monitor, ck, mood, halstead,'
                                                                                                    'jasome_files, jasome_methods, process_files, issues_files]. You can use the files under externals\configurations', default=r"externals\configurations\default.json")
        parser.add_argument('-s', '--select_verions', dest='select', action='store', help='the configuration to choose', default=-1, type=int)
        parser.add_argument('-n', '--num_verions', dest='num_versions', action='store', help='the number of versions to select', default=5, type=int)
        parser.add_argument('-t', '--versions_type', dest='versions_type', action='store', help='the versions type to select', default="Untyped")
        parser.add_argument('-f', '--free_choose', dest='free_choose', action='store_true', help='the versions type to select')
        parser.add_argument('-r', '--only_rest', dest='only_rest', action='store_true', help='extract only rest versions')
        parser.add_argument('rest', nargs=argparse.REMAINDER)
        args = parser.parse_args()
        self.github_user_name = args.github_user_name
        self.jira_url = args.jira_url
        if args.projects:
            self.list_projects()
        if args.choose:
            self.set_project_enum(args.choose)
        if args.github and args.jira:
            self.set_project(args.github, args.jira)
        if args.list_selected:
            self.extract()
            self.choose_versions(version_num=args.num_versions, algorithm=args.list_selected, version_type=VersionType[args.versions_type], strict=args.free_choose)
        if args.select != -1:
            self.set_version_selection(version_num=args.num_versions, algorithm='bin',
                                 version_type=VersionType[args.versions_type], strict=args.free_choose, selected_config=args.select)
            data_types = None
            if os.path.exists(args.data_types):
                with open(args.data_types) as f:
                    data_types = set(json.loads(f.read()))
            self.extract_metrics(args.rest, args.only_rest, data_types)


if __name__ == "__main__":
    m = Main()
    m.main()
