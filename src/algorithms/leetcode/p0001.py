from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    container = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in container:
            container[num] = i
        else:
            return [container[complement], i]
    return []
