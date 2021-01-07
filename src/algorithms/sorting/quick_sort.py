from src.algorithms.sorting.helper import prompt, swap


def partition(arr, low, high):
    """
    This function takes last element as pivot, places the pivot element
    at its correct position in sorted array, and places all smaller
    (smaller than pivot) to left of pivot and all greater elements
    to right of pivot
    """
    i = low - 1
    pivot = arr[high]
    # arr[:i] <= pivot <= arr[j:]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)
    # swapping the pivot element with the leftmost element greater than pivot
    swap(arr, i + 1, high)
    return i + 1


def quick_sort_part(arr, low, high):
    """
    arr[] --> Array to be sorted
    low  --> Starting index
    high  --> Ending index, len(arr)-1
    """
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quick_sort_part(arr, low, pi - 1)
        quick_sort_part(arr, pi + 1, high)
    return arr


def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    prompt(quick_sort)
