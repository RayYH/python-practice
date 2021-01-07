"""
https://leetcode.com/problems/last-stone-weight/

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y. The result of
this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of
weight y has new weight y-x.

At the end, there is at most 1 stone left. Return the weight of this stone
(or 0 if there are no stones left.)
"""
from src.algorithms.heaps.max_priority_queue import MaxPriorityQueue


def last_stone_weight(stones):
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[0]
    mpq = MaxPriorityQueue(arr=stones)
    max_val, second_max_val = mpq.heap_extract_max(), mpq.heap_extract_max()
    while True:
        new_weight = max_val - second_max_val
        if new_weight != 0:
            mpq.max_heap_insert(new_weight)
        max_val = mpq.heap_extract_max()
        if not max_val:
            if new_weight == 0:
                return 0
            return second_max_val
        second_max_val = mpq.heap_extract_max()
        if not second_max_val:
            return max_val
