def test_transpose_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    assert [[row[i] for row in matrix] for i in range(4)] == transposed
    assert transposed == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    assert list(zip(*matrix)) == [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
