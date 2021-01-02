def recursive_binary_search(sorted_list, target):
    # base case
    if len(sorted_list) == 0:
        return None

    # divide conquer
    mid = len(sorted_list) // 2
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] < target:
        return mid + recursive_binary_search(sorted_list[mid:], target)
    else:
        return recursive_binary_search(sorted_list[:mid], target)


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
