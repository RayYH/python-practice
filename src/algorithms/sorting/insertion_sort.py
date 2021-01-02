from src.algorithms.sorting.helper import prompt


def recursive_insertion_sort(collection, n):
    # base case
    if n <= 1:
        return collection

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


def insertion_sort_scanning_via_binary_search(collection):
    length = len(collection)
    if length >= 1:
        for j in range(1, length):
            # collection[:j] is sorted
            # we need to find correct index k which ensures
            # collection[k] <= collection[j] <= collection[k+1]
            current_value = collection[j]
            low = 0
            high = j - 1
            while low <= high:
                mid = (low + high) // 2
                if collection[mid] > current_value:
                    high = mid - 1
                else:
                    low = mid + 1

            # boundary check
            if low > length - 1:
                pos = (low + high - 1) // 2
            elif high < 0:
                pos = (low + high + 1) // 2
            else:
                pos = (low + high) // 2

            # pos is the location of current_value,
            # loop from pos+1 to j
            for k in range(j, pos + 1, -1):
                collection[k] = collection[k - 1]
            collection[pos + 1] = current_value

    return collection


if __name__ == '__main__':
    prompt(insertion_sort)
