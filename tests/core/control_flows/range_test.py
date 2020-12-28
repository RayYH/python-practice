from src.helper.ioh import captured_output, to_string


def test_generate_list_via_range_method():
    assert list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(range(2, 10)) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert list(range(0, 10, 2)) == [0, 2, 4, 6, 8]


def test_range_in_for_statement():
    genre = ['pop', 'rock', 'jazz']
    with captured_output() as (out, err):
        for i in range(len(genre)):
            print(genre[i], end=" ")
    assert to_string(out) == "pop rock jazz"
