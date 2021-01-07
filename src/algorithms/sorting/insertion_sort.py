from src.algorithms.sorting.helper import prompt


def recursive_insertion_sort(collection, n):
    if n <= 1:
        return collection
    recursive_insertion_sort(collection, n - 1)
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


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort_scanning_via_binary_search(collection):
    length = len(collection)
    if length >= 1:
        for j in range(1, length):
            current_value = collection[j]
            pos = binary_search(collection, current_value, 0, j - 1)
            i = j - 1
            while i >= 0 and i >= pos:
                collection[i + 1] = collection[i]
                i -= 1
            collection[i + 1] = current_value

    return collection


if __name__ == '__main__':
    prompt(insertion_sort)
