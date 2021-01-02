from src.algorithms.sorting.helper import prompt


def recursive_insertion_sort(collection, n):
    # base case
    if n <= 1:
        return

    # recursion call
    recursive_insertion_sort(collection, n - 1)

    # collection[1:n-2] are sorted
    last = collection[n - 1]
    pos = n - 2
    while pos >= 0 and collection[pos] > last:
        collection[pos + 1] = collection[pos]
        pos -= 1
    collection[pos + 1] = last

    return collection


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
