def find_smallest(unsorted):
    smallest_value = unsorted[0]
    smallest_key = 0
    for i in range(1, len(unsorted)):
        if unsorted[i] < smallest_value:
            smallest_value = unsorted[i]
            smallest_key = i
    return smallest_key


def selection_sort(collection):
    new_list = []
    for _ in range(len(collection)):
        smallest = find_smallest(collection)
        new_list.append(collection.pop(smallest))
    return new_list


def main():
    user_input = input("Enter numbers separated by a comma(,):\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))


if __name__ == '__main__':
    main()
