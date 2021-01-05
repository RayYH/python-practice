from src.algorithms.sorting.helper import is_sorted


def solution(arr):
    assert is_sorted(arr)
    length = len(arr)
    if length <= 1:
        return length
    left = 0
    right = length - 1
    ans = 0
    while left <= right:
        left_abs = abs(arr[left])
        right_abs = abs(arr[right])
        if left_abs > right_abs:
            ans += 1
            while left <= right and abs(arr[left]) == left_abs:
                left += 1
        elif left_abs < right_abs:
            ans += 1
            while left <= right and abs(arr[right]) == right_abs:
                right -= 1
        else:
            ans += 1
            while left <= right and abs(arr[left]) == left_abs:
                left += 1
            while left <= right and abs(arr[right]) == right_abs:
                right -= 1
    return ans
