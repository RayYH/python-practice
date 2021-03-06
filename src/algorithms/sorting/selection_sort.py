from src.algorithms.sorting.helper import prompt, swap, less_than


def selection_sort(collection):
    for j in range(0, len(collection) - 1):
        smallest = j
        for i in range(j + 1, len(collection)):
            if less_than(collection, i, smallest):
                smallest = i
        swap(collection, j, smallest)
    return collection


if __name__ == '__main__':
    prompt(selection_sort)
