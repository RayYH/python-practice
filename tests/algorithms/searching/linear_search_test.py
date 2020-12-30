from src.algorithms.searching.linear_search import linear_search


def test_binary_search():
    collection = [1, 3, 5, 11, 32, 98, 7, 9]
    assert linear_search(collection, 3) == 1
    assert linear_search(collection, 9) == len(collection) - 1
    assert not linear_search(collection, 90)
