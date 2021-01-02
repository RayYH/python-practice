from typing import List
from src.algorithms.sorting.merge_sort import merge_sort


# Introduction to Algorithms (3th) 2.3-7
def exists(nums: List[int], target: int) -> bool:
    # edge case
    if len(nums) < 2:
        return False

    # sort first - using n lgn time algorithm
    nums = merge_sort(nums)

    # using two pointers
    low = 0
    high = len(nums) - 1
    while low < high:
        current_sum = nums[low] + nums[high]
        if current_sum == target:
            return True
        elif current_sum < target:
            low += 1
        else:
            high -= 1
    return False


# https://leetcode.com/problems/two-sum/
def two_sum(nums: List[int], target: int) -> List[int]:
    container = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in container:
            container[num] = i
        else:
            return [container[complement], i]
    return []
