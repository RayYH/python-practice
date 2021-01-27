from src.algorithms.arrays.groups_of_special_equivalent_strings import \
    num_of_special_equivalent_strings


def test_solution():
    assert num_of_special_equivalent_strings(
        ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]) == 3
    assert num_of_special_equivalent_strings(
        ["abc", "acb", "bac", "bca", "cab", "cba"]) == 3
