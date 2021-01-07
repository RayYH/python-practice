"""
An array A that represents a heap is an object with two attributes: A:length,
which (as usual) gives the number of elements in the array, and A:heap-size,
which represents how many elements in the heap are stored within array A.

Notice python is 0-based array.
"""
from src.algorithms.sorting.helper import swap


def parent(i):
    """
    Compute the parent index of the node at index i.
    """
    return (i - 1) // 2


def left(i):
    """
    Compute the left child index of the node at index i.
    """
    return 2 * i + 1


def right(i):
    """
    Compute the right child index of the node at index i.
    """
    return 2 * i + 2


def max_heapify(arr, heap_size, i):
    left_index = left(i)
    right_index = right(i)
    if left_index < heap_size and arr[left_index] > arr[i]:
        largest_index = left_index
    else:
        largest_index = i
    if right_index < heap_size and arr[right_index] > arr[largest_index]:
        largest_index = right_index
    if largest_index != i:
        swap(arr, i, largest_index)
        max_heapify(arr, heap_size, largest_index)


def build_max_heap(arr):
    length = len(arr)
    heap_size = length
    for i in range(length // 2, -1, -1):
        max_heapify(arr, heap_size, i)
