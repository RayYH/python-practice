import os
from src.helper.bash import run_bash


def test_run_pwd_command():
    if os.name == 'nt':
        pass
    else:
        res = run_bash('pwd')
        assert not res['error']
        assert res['output'].startswith('/')


def test_run_invalid_command():
    if os.name == 'nt':
        pass
    else:
        res = run_bash("INVALID_COMMAND")
        assert not res['output']
        assert res['error'] == 'cannot exec command: INVALID_COMMAND'
