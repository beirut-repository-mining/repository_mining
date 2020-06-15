import argparse
from projects import ProjectName, Project
from data_extractor import DataExtractor
from version_selector import VersionType


class Main():
    def __init__(self):
        self.project = None
        self.extractor = None

    def list_projects(self):
        print("\n".join(list(map(lambda e: "{0}: {1}".format(e.name, e.value.description()), ProjectName))))

    def extract(self):
        self.extractor = DataExtractor(self.project)

    def get_project(self, github, jira):
        return Project(github, jira)

    def main(self):
        parser = argparse.ArgumentParser(description='Execute project data')
        parser.add_argument('-p', '--projects', dest='projects', action='store_const', const=True, default=False,
                            help='list all aleready defined projects')
        parser.add_argument('-p', '--projects', dest='projects', action='store_const', const=True, default=False,
                            help='list all aleready defined projects')
        parser.add_argument('-c', '--choose', dest='choose', action='store', help='choose a project to extract')
        parser.add_argument('-g', '--github_url', dest='github', action='store', help='the git link to the project to extract')
        parser.add_argument('-j', '--jira_url', dest='jira', action='store', help='the jira link to the project to extract')
        parser.add_argument('-s', '--select_verions', dest='select', action='store', help='the algorithm to select the versions : [bin, quadratic]', default='quadratic')
        parser.add_argument('-n', '--num_verions', dest='num_versions', action='store', help='the number of versions to select', default=5, type=int)
        parser.add_argument('-t', '--versions_type', dest='versions_type', action='store', help='the versions type to select', default="Untyped")
        args = parser.parse_args()
        if args.projects:
            self.list_projects()
        if args.choose:
            self.project = ProjectName[args.choose]
            self.extract()
        if args.github and args.jira:
            self.project = self.get_project(args.github, args.jira)
            self.extract()
        if args.select:
            self.extractor.choose_versions(version_num=args.num_versions, algorithm=args.select, strict="false", version_type=VersionType[args.versions_type])



if __name__ == "__main__":
    Main().main()