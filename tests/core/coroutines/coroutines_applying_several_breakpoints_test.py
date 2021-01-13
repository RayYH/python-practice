from src.helper.ioh import captured_output, to_string


def joint_print():
    while True:
        part_1 = (yield)
        part_2 = (yield)
        print("{} {}".format(part_1, part_2))


def test_joint_print():
    with captured_output() as (out, err):
        cor = joint_print()
        next(cor)
        cor.send("So Far")
        cor.send("So Good")
    assert to_string(out) == "So Far So Good"
