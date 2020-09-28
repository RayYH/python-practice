from src.helper.io import captured_output, to_string
from src.core.control_flows.break_continue_statement import break_usage, continue_usage


def test_break_usage():
    with captured_output() as (out, err):
        break_usage()
    assert to_string(out) == "str"


def test_continue_usage():
    with captured_output() as (out, err):
        continue_usage()
    assert to_string(out) == "sting"
