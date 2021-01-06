from src.algorithms.heaps.last_stone_weight import last_stone_weight


def test_solution():
    assert last_stone_weight([3, 7, 2]) == 2
    assert last_stone_weight([2, 2]) == 0
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
