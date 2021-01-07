"""
A max-priority queue implementation.

Introduction to Algorithms section 6.5
"""
from src.algorithms.heaps.heaps import max_heapify, parent, build_max_heap
from src.algorithms.sorting.heap_sort import swap
import sys


class MaxPriorityQueue(object):
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr)
        build_max_heap(self.arr)

    def heap_maximum(self):
        """
        Returns the element of arr with the largest value.
        """
        if self.heap_size < 1:
            return None
        return self.arr[0]

    def heap_extract_max(self):
        """
        Removes and returns the element of arr with the largest value.
        """
        if self.heap_size < 1:
            return None
        max_val = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        max_heapify(self.arr, self.heap_size, 0)
        return max_val

    def heap_increase_key(self, i, key) -> bool:
        """
        Increases the value of element at index i to the new value key.
        """
        if key < self.arr[i]:
            return False
        self.arr[i] = key
        while 0 < i and self.arr[parent(i)] < self.arr[i]:
            swap(self.arr, i, parent(i))
            i = parent(i)
        return True

    def max_heap_insert(self, key):
        """
        Inserts one element with value key into the set.
        """
        self.heap_size += 1
        self.arr[self.heap_size - 1] = -sys.maxsize
        self.heap_increase_key(self.heap_size - 1, key)
