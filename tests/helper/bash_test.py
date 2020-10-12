import os
from src.helper.bash import run_bash


def test_run_bash():
    if os.name == 'nt':
        assert True
    else:
        res = run_bash('pwd')
        assert not res['error']
        assert res['output'].startswith('/')
