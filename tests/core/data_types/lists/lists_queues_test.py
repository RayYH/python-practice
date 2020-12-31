from collections import deque


def test():
    queue = deque(["Eric", "John", "Michael"])
    assert '{}'.format(queue) == "deque(['Eric', 'John', 'Michael'])"
    queue.append("Terry")
    assert '{}'.format(queue) == "deque(['Eric', 'John', 'Michael', 'Terry'])"
    item = queue.popleft()
    assert item == 'Eric'
    assert '{}'.format(queue) == "deque(['John', 'Michael', 'Terry'])"
    item = queue.pop()
    assert item == 'Terry'
    assert '{}'.format(queue) == "deque(['John', 'Michael'])"
