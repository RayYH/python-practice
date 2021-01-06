from src.algorithms.sorting.heap_sort import max_heapify, parent, build_max_heap
from src.algorithms.sorting.heap_sort import swap
import sys


class MaxPriorityQueue(object):
    def __init__(self, arr):
        self.arr = arr
        length = len(arr)
        self.heap_size = length
        build_max_heap(self.arr)

    def heap_maximum(self):
        if self.heap_size < 1:
            return None
        return self.arr[0]

    def heap_extract_max(self):
        if self.heap_size < 1:
            return None
        max_val = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        max_heapify(self.arr, self.heap_size, 0)
        return max_val

    def heap_increase_key(self, i, key):
        if key < self.arr[i]:
            # new key is smaller than current key
            return False
        self.arr[i] = key
        while 0 < i and self.arr[parent(i)] < self.arr[i]:
            swap(self.arr, i, parent(i))
            i = parent(i)

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.arr[self.heap_size - 1] = -sys.maxsize
        self.heap_increase_key(self.heap_size - 1, key)
