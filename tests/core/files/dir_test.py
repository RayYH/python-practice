import os
import shutil

TEST_DIRECTORY_RELATIVE_PATH = "/tmp/pytest"


def test_get_cwd_and_chdir():
    # os.getcwd() returns current working directory!
    assert os.getcwd()
    current_dir = os.getcwd()
    os.chdir("/")
    assert os.getcwd() == "/"
    os.chdir(current_dir)
    assert os.path.basename(__file__)


def test_dir_operations():
    os.mkdir(TEST_DIRECTORY_RELATIVE_PATH)
    assert len(os.listdir(TEST_DIRECTORY_RELATIVE_PATH)) == 0
    os.rename(TEST_DIRECTORY_RELATIVE_PATH,
              TEST_DIRECTORY_RELATIVE_PATH + '-new')
    assert len(os.listdir(TEST_DIRECTORY_RELATIVE_PATH + '-new')) == 0
    os.rename(TEST_DIRECTORY_RELATIVE_PATH + '-new',
              TEST_DIRECTORY_RELATIVE_PATH)
    # remove a empty directory
    os.rmdir(TEST_DIRECTORY_RELATIVE_PATH)
    os.mkdir(TEST_DIRECTORY_RELATIVE_PATH)
    # remove a non-empty directory
    shutil.rmtree(TEST_DIRECTORY_RELATIVE_PATH)
