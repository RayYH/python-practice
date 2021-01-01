from src.algorithms.sorting.helper import prompt


def insertion_sort(collection):
    length = len(collection)
    if length >= 1:
        for j in range(1, length):
            current_value = collection[j]
            i = j - 1
            while i >= 0 and collection[i] > current_value:
                collection[i + 1] = collection[i]
                i -= 1
            collection[i + 1] = current_value
    return collection


if __name__ == '__main__':
    prompt(insertion_sort)
