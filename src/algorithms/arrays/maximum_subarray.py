"""
https://leetcode-cn.com/problems/maximum-subarray/
https://leetcode.com/problems/maximum-subarray/
"""
import sys


def find_max_crossing_sub_array(arr, low, mid, high):
    left_sum = right_sum = 0 - sys.maxsize
    max_left = mid
    max_right = mid + 1

    # arr[mid, mid-1, .. low]
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    # arr[mid+1, mid+2, .. high]
    current_sum = 0
    for j in range(mid + 1, high + 1):
        current_sum += arr[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(
            arr, low, mid
        )
        right_low, right_high, right_sum = find_maximum_subarray(
            arr, mid + 1, high
        )
        cross_low, cross_high, cross_sum = find_max_crossing_sub_array(
            arr, low, mid, high
        )
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def maximum_subarray_via_divide_and_conquer(arr):
    return find_maximum_subarray(arr, 0, len(arr) - 1)[2]


# dp solution
def maximum_subarray(nums):
    max_val = -sys.maxsize - 1
    res = 0
    n = len(nums)
    for i in range(n):
        res += nums[i]
        if res > max_val:
            max_val = res

        if res < 0:
            res = 0

    return max_val
