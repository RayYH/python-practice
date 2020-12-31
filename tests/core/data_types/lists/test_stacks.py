def test():
    stack = [3, 4, 5]
    assert stack
    stack.append(6)
    stack.append(7)
    assert stack == [3, 4, 5, 6, 7]
    stack.pop()
    assert stack == [3, 4, 5, 6]
    stack.pop()
    assert stack == [3, 4, 5]
