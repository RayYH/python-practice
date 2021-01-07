"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest
sum and return its sum.
"""
import sys


def find_max_crossing_sub_array(arr, low, mid, high):
    """
    Returns a tuple containing the indices demarcating a maximum subarray
    that crosses the midpoint, along with the sum of the values in a
    maximum subarray.
    """
    l_sum = r_sum = -sys.maxsize - 1
    l_best_index = mid
    r_best_index = mid + 1

    # check the left part
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > l_sum:
            l_sum = current_sum
            l_best_index = i

    # check the right part
    current_sum = 0
    for j in range(mid + 1, high + 1):
        current_sum += arr[j]
        if current_sum > r_sum:
            r_sum = current_sum
            r_best_index = j

    return l_best_index, r_best_index, l_sum + r_sum


def find_maximum_subarray(arr, low, high):
    """
    Find a maximum subarray crossing the midpoint in time linear in the size
    of the subarray arr[low:high]
    """
    if high == low:
        # one element
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        l_low, l_high, l_sum = find_maximum_subarray(arr, low, mid)
        r_low, r_high, r_sum = find_maximum_subarray(arr, mid + 1, high)
        c_low, c_high, c_sum = find_max_crossing_sub_array(arr, low, mid, high)
        if l_sum >= r_sum and l_sum >= c_sum:
            return l_low, l_high, l_sum
        elif r_sum >= l_sum and r_sum >= c_sum:
            return r_low, r_high, r_sum
        else:
            return c_low, c_high, c_sum


def divide_and_conquer_solution(arr):
    return find_maximum_subarray(arr, 0, len(arr) - 1)[2]


def kadane_algorithm_solution(nums):
    """
    Kadane's algorithm (DP solution)

    Apparently, this is a optimization problem, which can be usually
    solved by DP.

    f(i): max sum of subarray which ends with nums[i]
    f(0) = nums[0]
    f(1) = max(f(0), 0) + nums[1]
    ...
    f(j+1) = max(f(j), 0) + nums[j+1]) -- 0 means f(j+1) = nums[j+1]
    """
    best_sum = -sys.maxsize - 1
    current_sum = 0
    n = len(nums)
    for i in range(n):
        current_sum += nums[i]
        if current_sum > best_sum:
            best_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return best_sum


def brute_force_solution(nums):
    """
    Brute-Force solution
    """
    ans = -sys.maxsize - 1
    for i in range(0, len(nums)):
        # max_val holds the max val of arr[i..k] where i must be included
        # and k maybe i+1, i+2, i+3, ... len(arr)-1
        max_val = nums[i]
        # current_sum holds the current value of arr[i..j]
        current_sum = nums[i]
        for j in range(i + 1, len(nums)):
            current_sum += nums[j]
            if current_sum > max_val:
                max_val = current_sum
        if max_val > ans:
            ans = max_val
    return ans
