from src.algorithms.sorting.helper import swap, prompt
from src.algorithms.heaps.heaps import build_max_heap, max_heapify


def heap_sort(arr):
    build_max_heap(arr)
    length = len(arr)
    heap_size = length
    for i in range(length - 1, 0, -1):
        swap(arr, i, 0)
        heap_size -= 1
        max_heapify(arr, heap_size, 0)
    return arr


if __name__ == '__main__':
    prompt(heap_sort)
