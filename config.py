import configparser
import os
import tempfile
import pathlib


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        cwd = pathlib.Path(__file__).parent.absolute()
        config_path = cwd.joinpath(r"config.ini")
        self.config.read(config_path)

    @staticmethod
    def get_temp_path(path=""):
        if path == "":
            return tempfile.gettempdir()
        return os.path.join(tempfile.gettempdir(), path)

    @staticmethod
    def get_work_dir_path(path=""):
        cwd = pathlib.Path(__file__).parent.absolute()
        if path == "":
            return cwd
        return cwd.joinpath(path)

    @staticmethod
    def assert_dir_exists(dir_path):
        path = pathlib.Path(dir_path)
        path.mkdir(parents=True, exist_ok=True)
        return dir_path
