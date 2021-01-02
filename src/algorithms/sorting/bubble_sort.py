from src.algorithms.sorting.helper import swap, prompt, less_than


def bubble_sort(collection):
    n = len(collection)
    last_swapped_index = n - 1
    for i in range(0, n - 1):
        current_swapped_index = -1
        for j in range(0, last_swapped_index):
            if less_than(collection, j + 1, j):
                current_swapped_index = j
                swap(collection, j + 1, j)
        if current_swapped_index == -1:
            break
        else:
            last_swapped_index = current_swapped_index

    return collection


if __name__ == '__main__':
    prompt(bubble_sort)
