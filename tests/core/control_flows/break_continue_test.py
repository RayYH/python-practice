from src.helper.ioh import captured_output, to_string


def break_usage():
    for letter in "string":
        if letter == "i":
            break
        print(letter, sep="", end="")


def test_break_usage():
    with captured_output() as (out, err):
        break_usage()
    assert to_string(out) == "str"


def continue_usage():
    for letter in "string":
        if letter == "r":
            continue
        print(letter, sep="", end="")


def test_continue_usage():
    with captured_output() as (out, err):
        continue_usage()
    assert to_string(out) == "sting"
