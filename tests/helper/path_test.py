from src.helper.path import get_project_root_dir


def test_get_project_root_dir():
    assert get_project_root_dir().endswith('practice')
