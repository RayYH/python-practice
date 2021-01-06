import json

TEST_FILE_RELATIVE_PATH = "/tmp/pytest.txt"


def test_json_dumps():
    assert json.dumps([1, 'simple', 'list']) == '[1, "simple", "list"]'
    assert json.dumps(True) == 'true'
    assert json.dumps(False) == 'false'
    assert json.dumps({"name": "Ray", "age": 25}) == \
           '{"name": "Ray", "age": 25}'


def test_json_dump_and_load():
    with open(TEST_FILE_RELATIVE_PATH, 'w') as f:
        json.dump({"name": "Ray", "age": 25}, f)

    with open(TEST_FILE_RELATIVE_PATH, 'r') as f:
        assert json.load(f) == {"name": "Ray", "age": 25}


def test_json_loads():
    assert json.loads('{"name": "Ray", "age": 25}') == \
           {"name": "Ray", "age": 25}
