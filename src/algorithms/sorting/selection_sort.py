def selection_sort(collection):
    for j in range(0, len(collection) - 1):
        smallest = j
        for i in range(j + 1, len(collection)):
            if collection[i] < collection[smallest]:
                smallest = i
        collection[smallest], collection[j] = \
            collection[j], collection[smallest]
    return collection


def main():
    user_input = input("Enter numbers separated by a comma(,):\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))


if __name__ == '__main__':
    main()
