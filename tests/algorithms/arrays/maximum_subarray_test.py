from src.algorithms.arrays.maximum_subarray \
    import maximum_subarray_via_divide_and_conquer, maximum_subarray


def test_maximum_subarray_via_divide_and_conquer():
    assert maximum_subarray_via_divide_and_conquer(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maximum_subarray_via_divide_and_conquer([1]) == 1
    assert maximum_subarray_via_divide_and_conquer([0]) == 0
    assert maximum_subarray_via_divide_and_conquer([-1]) == -1
    assert maximum_subarray_via_divide_and_conquer([-2147483647
                                                    ]) == -2147483647


def test_maximum_subarray():
    assert maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maximum_subarray([1]) == 1
    assert maximum_subarray([0]) == 0
    assert maximum_subarray([-1]) == -1
    assert maximum_subarray([-2147483647]) == -2147483647
