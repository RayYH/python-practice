from src.algorithms.sorting.helper import prompt, is_sorted


def merge_sort(collection):
    if len(collection) < 2:
        return collection
    mid = (len(collection)) // 2
    left_list = merge_sort(collection[:mid])
    right_list = merge_sort(collection[mid:])
    assert is_sorted(left_list)
    assert is_sorted(right_list)
    result = []
    i = j = k = 0
    left_len = len(left_list)
    right_len = len(right_list)
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
