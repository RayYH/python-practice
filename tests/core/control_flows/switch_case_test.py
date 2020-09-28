from src.core.control_flows.switch_case import switched, switched_with_defaults


def test_switch_case():
    choices = {"a": 1, "b": 2, "c": 3}
    assert switched("a", choices) == 1
    assert switched("b", choices) == 2
    assert switched("c", choices) == 3
    assert not switched("d", choices)
    assert switched_with_defaults("d", choices, 4) == 4
