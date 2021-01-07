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
    """
    In a max-heap, the max-heap property is that for every node i other than
    the root, arr[parent[i]] >= arr[i], that is, the value of a node is at
    most the value of its parent.

    When this is called, max_heapify assumes that the binary trees rooted at
    left(i) and right(i) are max-heaps, but that arr[i] might be smaller
    than its children, thus violating the max-heap property.

    max_heapify lets the value at arr[i] “float down” in the max-heap so that
    the subtree rooted at index i obeys the max-heap property.
    """
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
        # At this point, the subtree rooted at largest_index might violate
        # the max-heap property, we need to call max_heapify recursively
        # on that subtree
        max_heapify(arr, heap_size, largest_index)
    # if arr[i] is largest, the subtree rooted at node i is already a max-heap


def build_max_heap(arr):
    """
    convert an array arr into a max-heap in a bottom-up manner.
    """
    length = len(arr)
    heap_size = length
    for i in range(length // 2, -1, -1):
        max_heapify(arr, heap_size, i)
