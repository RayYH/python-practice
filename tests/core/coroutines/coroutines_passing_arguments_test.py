from src.helper.ioh import captured_output, to_string


def filter_line(num):
    while True:
        line = (yield)
        if num in line:
            print(line)


def test_filter_line():
    with captured_output() as(out, err):
        cor = filter_line("33")
        next(cor)
        cor.send("Jessica, age:24")
        cor.send("Marco, age:33")
        cor.send("Filipe, age:55")
    assert to_string(out) == "Marco, age:33"
