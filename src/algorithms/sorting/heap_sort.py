from src.algorithms.sorting.helper import swap, prompt


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
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
