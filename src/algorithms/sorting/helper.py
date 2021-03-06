from typing import Callable, List


def count_equals(sorted_list: List, unsorted_list: List):
    for v in sorted_list:
        if sorted_list.count(v) != unsorted_list.count(v):
            return False
    return True


def is_sorted(collection: List):
    return all(collection[i] <= collection[i + 1]
               for i in range(len(collection) - 1))


def prompt(sort_algorithm: Callable, *args):
    user_input = input("Enter numbers separated by a comma(,):\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(sort_algorithm(unsorted, *args))


def swap(collection: List, a, b):
    collection[a], collection[b] = collection[b], collection[a]


def less_than(collection: List, a, b):
    return collection[a] < collection[b]
