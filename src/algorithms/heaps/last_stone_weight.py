"""
https://leetcode-cn.com/problems/last-stone-weight/
"""
from src.algorithms.heaps.max_priority_queue import MaxPriorityQueue


def last_stone_weight(stones):
    max_priority_queue = MaxPriorityQueue(arr=stones)
    max_val = max_priority_queue.heap_extract_max()
    if not max_val:
        return 0
    second_max_val = max_priority_queue.heap_extract_max()
    if not second_max_val:
        return max_val
    while True:
        new_weight = max_val - second_max_val
        if new_weight != 0:
            max_priority_queue.max_heap_insert(new_weight)
        max_val = max_priority_queue.heap_extract_max()
        if not max_val:
            if new_weight == 0:
                return 0
            return second_max_val
        second_max_val = max_priority_queue.heap_extract_max()
        if not second_max_val:
            return max_val
