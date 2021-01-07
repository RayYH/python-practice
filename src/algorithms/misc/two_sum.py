from typing import List


# Introduction to Algorithms (3th) 2.3-7
def exists(nums: List[int], target: int) -> bool:
    # edge case
    if len(nums) < 2:
        return False

    # sort first
    nums.sort()

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


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    https://leetcode.com/problems/two-sum/

    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

    You can return the answer in any order.
    """
    container = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in container:
            container[num] = i
        else:
            return [container[complement], i]
    return []
