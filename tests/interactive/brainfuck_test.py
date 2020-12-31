from src.interactive.brainfuck import run
from src.helper.ioh import captured_output, to_string
from src.helper.path import get_test_resources_dir


def test_brainfuck():
    with captured_output() as (out, err):
        run(get_test_resources_dir() + '/bfs/hello.bf')
    assert to_string(out) == 'Hello World!'
