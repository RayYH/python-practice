def merge_inversions(arr, p, q, r):
    """
    Merge sorted array arr[p:q] and arr[q:r] such that arr[p:r] is sorted
    """
    left, right = arr[p:q].copy(), arr[q:r].copy()
    len_left, len_right = len(left), len(right)
    # i - current index of left part
    # j - current index of right part
    i = j = 0
    inversions_count = 0
    k = p
    # whether we have counted the merge-inversions involving right[j]
    # think about two arrays: [4, 5, 6] (left) and [1, 2, 3] (right)
    # we compare the first element 4 in left array and the first
    # element 1 in right array, since 4 (left) > 1 (right), all
    # elements in the left array after 4 should be counted
    # because 6 > 5 > 4 > 1.
    counted = False
    while i < len_left and j < len_right:
        # count inversions first, then move right pointer
        if not counted and right[j] < left[i]:
            inversions_count += len_left - i
            counted = True
        # If left[i] <= right[j], there's no need to move i and no new
        # inversions occur, just skip, but if left[i] > right[j], new
        # inversions occur, we should count previous inversions of
        # right[j-1] and reset the counted flag.
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            counted = False
            # At here, inversions of arr[j] has already been counted!
            # we just move right pointer and reset the counted flag
        k += 1
    remain_elements = left[i:] + right[j:]
    arr[k:r] = remain_elements

    return inversions_count


def count_inversions(arr, p, r):
    """
    Count the inversions of arr[p:r].
    """
    inversions_count = 0
    # At least two elements in arr[p:r]
    if p < r - 1:
        q = (p + r) // 2
        inversions_count += count_inversions(arr, p, q)
        inversions_count += count_inversions(arr, q, r)
        inversions_count += merge_inversions(arr, p, q, r)
    # p >= r - 1, think about arr[r-1,r] which contains 1 element
    # So at here, at most one elements in arr returns 0 directly
    return inversions_count


def inversions(arr):
    """
    Let A[1..n] be an array of n distinct numbers.
    If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A.

    Give an algorithm that determines the number of inversions in any
    permutation on n elements in O(n lgn) worst-case time.

    Hint: merge sort.
    """
    return count_inversions(arr, 0, len(arr))
