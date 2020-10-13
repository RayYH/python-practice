import os


def get_project_root_dir():
    return os.path.dirname(os.path.abspath(__file__ + "/../../"))


def get_test_resources_dir():
    return get_project_root_dir() + '/tests/resources'
