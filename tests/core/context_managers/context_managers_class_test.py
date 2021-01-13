class File(object):
    def __init__(self, filename, mode):
        self.file_obj = open(filename, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


def test_with_statements():
    tmp_file = "/tmp/pytest.txt"
    with File(tmp_file, mode='r') as opened_file:
        assert opened_file
