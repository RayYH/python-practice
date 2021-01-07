from typing import List


def all_squares(nums: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/
    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.
    """
    squares = [0] * len(nums)
    current_index = len(nums) - 1
    left_index, right_index = 0, len(nums) - 1
    while left_index <= right_index:
        left_abs, right_abs = abs(nums[left_index]), abs(nums[right_index])
        if left_abs >= right_abs:
            squares[current_index] = left_abs * left_abs
            left_index += 1
        else:
            squares[current_index] = right_abs * right_abs
            right_index -= 1
        current_index -= 1
    return squares


def distinct_count(nums):
    """
    Return the distinct counts of squares.
    """
    length = len(nums)
    if length <= 1:
        return length
    left, right = 0, length - 1
    ans = 0
    while left <= right:
        left_abs = abs(nums[left])
        right_abs = abs(nums[right])
        if left_abs > right_abs:
            ans += 1
            while left <= right and abs(nums[left]) == left_abs:
                left += 1
        elif left_abs < right_abs:
            ans += 1
            while left <= right and abs(nums[right]) == right_abs:
                right -= 1
        else:
            ans += 1
            while left <= right and abs(nums[left]) == left_abs:
                left += 1
            while left <= right and abs(nums[right]) == right_abs:
                right -= 1
    return ans
