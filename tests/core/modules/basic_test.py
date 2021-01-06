import src
import sys
from src.helper.path import get_project_root_dir


def test_name():
    assert src.__name__ == 'src'


def test_modules_search_path():
    assert get_project_root_dir() in sys.path
