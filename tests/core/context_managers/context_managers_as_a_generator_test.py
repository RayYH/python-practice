from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


def test_with_statements():
    tmp_file = "/tmp/pytest.txt"
    with open_file(tmp_file) as f:
        assert f
