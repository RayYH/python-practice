from src.helper.io import captured_output, to_string


# Enumerate() method adds a counter to an iterable and returns
# it in a form of enumerate object.
def test_enumerate():
    fruits = ['apple', 'orange', 'banana']
    greeting = 'hello'
    e1 = enumerate(fruits)
    # changing start index to 2 from 0
    e2 = enumerate(greeting, 2)
    assert '{}'.format(type(e1)) == "<class 'enumerate'>"
    assert '{}'.format(type(e2)) == "<class 'enumerate'>"
    assert list(e1) == [(0, 'apple'), (1, 'orange'), (2, 'banana')]
    assert list(e2) == [(2, 'h'), (3, 'e'), (4, 'l'), (5, 'l'), (6, 'o')]
    with captured_output() as (out, err):
        # MUST use enumerate(fruits) instead of e1
        for ele in enumerate(fruits):
            print(ele)
        for count, ele in enumerate(greeting, 2):
            print(count, ele)
    assert (to_string(out)) == '''(0, 'apple')
(1, 'orange')
(2, 'banana')
2 h
3 e
4 l
5 l
6 o'''
