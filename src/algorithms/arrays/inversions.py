def merge_inversions(arr, p, q, r):
    left, right = arr[p:q].copy(), arr[q:r].copy()
    left_len, right_len = len(left), len(right)
    i = j = inversions = 0
    k = p
    counted = False
    while i < left_len and j < right_len:
        if not counted and right[j] < left[i]:
            inversions += left_len - i
            counted = True
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            counted = False
        k += 1
    remain_elements = left[i:] + right[j:]
    arr[k:r] = remain_elements

    return inversions


def count_inversions(arr, p, r):
    # wht not p < r? since, we use q instead of q+1
    inversions = 0
    if p < r - 1:
        q = (p + r) // 2
        inversions += count_inversions(arr, p, q)  # arr[p:q] is sorted
        inversions += count_inversions(arr, q, r)  # arr[q:r] is sorted
        inversions += merge_inversions(arr, p, q, r)
    return inversions


def number_of_inversions(arr):
    """
    Let A[1..n] be an array of n distinct numbers.
    If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A.

    Give an algorithm that determines the number of inversions in any
    permutation on n elements in O(n lgn) worst-case time.

    Hint: merge sort.
    """
    return count_inversions(arr, 0, len(arr))
