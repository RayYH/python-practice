from src.helper.ioh import captured_output, to_string


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


def test_grep():
    with captured_output() as (out, err):
        search = grep('coroutine')
        next(search)
        # Output: Searching for coroutine
        search.send("I love you")
        search.send("Don't you love me?")
        search.send("I love coroutines instead!")
        # Output: I love coroutines instead!
        search.close()
    assert to_string(out) == '''Searching for coroutine
I love coroutines instead!'''
