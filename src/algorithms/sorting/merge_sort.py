from src.algorithms.sorting.helper import prompt


def merge(arr, p, q, r):
    """
    arr is an array and p, q, and r are indices into the array such that
    p <= q < r.

    The procedure assumes that the subarrays arr[p..q] and arr[q+1..r]
    are in sorted order. It merges them to form a single sorted
    subarray that replaces the current subarray A[p..r].
    """
    left, right = arr[p:q].copy(), arr[q:r].copy()
    left_len, right_len = len(left), len(right)
    i = j = 0
    k = p
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    remain_elements = left[i:] + right[j:]
    arr[k:r] = remain_elements

    return arr


def merge_sort_part(arr, p, r):
    if p < r - 1:
        q = (p + r) // 2
        merge_sort_part(arr, p, q)
        merge_sort_part(arr, q, r)
        merge(arr, p, q, r)
    return arr


def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # recursive calls
    mid = (len(arr)) // 2
    left_list, right_list = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # handle sub result - merge
    result = []
    i = j = k = 0
    left_len, right_len = len(left_list), len(right_list)
    while i < left_len and j < right_len:
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
        k += 1
    result += left_list[i:]
    result += right_list[j:]
    return result


if __name__ == '__main__':
    prompt(merge_sort)
