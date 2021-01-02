from typing import Callable, List


def is_sorted(collection: List):
    return all(collection[i] <= collection[i + 1]
               for i in range(len(collection) - 1))


def prompt(sort_algorithm: Callable):
    user_input = input("Enter numbers separated by a comma(,):\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(sort_algorithm(unsorted))


def swap(collection: List, a, b):
    collection[a], collection[b] = collection[b], collection[a]


def less_than(collection: List, a, b):
    return collection[a] < collection[b]
