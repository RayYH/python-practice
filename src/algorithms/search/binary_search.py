"""
1. set l=0 and r=n-1
2. if l>R the search terminates as unsuccessful.
3. set m (the position of the middle element) to the floor of (l+r)/2
   which is the greatest integer less than or equal to (l+r)/2.
4. if a[m] < t, set l to m+1 and go to step 2.
5. if a[m] > t, set r to m-1 and go to step 2.
6. now a[m] = t, the search is done, return m.
"""


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        if sorted_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return None
