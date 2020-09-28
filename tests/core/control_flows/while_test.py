from src.core.control_flows.while_statement \
    import sum_from_1_to_n, while_loop_with_else
from src.helper.io import captured_output, to_string


def test_sum_from_1_to_n():
    assert sum_from_1_to_n(10) == 55
    assert sum_from_1_to_n(3) == 6


def test_while_loop_with_else():
    with captured_output() as (out, err):
        while_loop_with_else()
    assert to_string(out) == "Inside loop " * 3 + "Inside else"
