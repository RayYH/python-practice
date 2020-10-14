TEST_FILE_RELATIVE_PATH = "/tmp/pytest.txt"


class File(object):
    def __init__(self, filename, mode):
        self.file_obj = open(filename, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


def test_file():
    with open(TEST_FILE_RELATIVE_PATH, "w") as f:
        assert f
    with File(TEST_FILE_RELATIVE_PATH, mode='r') as file_handler:
        assert file_handler
