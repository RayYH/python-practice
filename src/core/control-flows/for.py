def for_in_loop():
    """
    Program to find the sum of all numbers stored in a list
    """
    # List of numbers
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
    # variable to store the sum
    sum_num = 0
    # iterate over the list
    for val in numbers:
        sum_num = sum_num + val
    print("The sum is", sum_num)


def range_usage():
    # <class 'range'>
    print(type(range(10)))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(10)))
    # [2, 3, 4, 5, 6, 7]
    print(list(range(2, 8)))
    # [2, 5, 8, 11, 14, 17]
    print(list(range(2, 20, 3)))
    genre = ['pop', 'rock', 'jazz']
    # iterate over the list using index
    for i in range(len(genre)):
        print("I like", genre[i])


def for_loop():
    """
    python does not support (i = 0; i < 10; i++) syntax
    but you can use for-range syntax to make it
    """
    # (i = 0; i < 10; i++)
    for i in range(0, 10, 1):
        # 0 1 2 3 4 5 6 7 8 9
        print("{} ".format(i), sep="", end="")
    print()
    # (i = 0; i < 10; i+=2)
    for i in range(0, 10, 2):
        # 0 2 4 6 8
        print("{} ".format(i), sep="", end="")
    print()


def for_loop_with_else():
    digits = [0, 1, 5]
    for i in digits:
        print(i)
    # when loop is done
    else:
        print("No items left.")
    # program to display student's marks from record
    student_name = 'Ray'
    marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print('No entry with that name found.')


def main():
    for_in_loop()
    for_loop()
    range_usage()
    for_loop_with_else()


if __name__ == '__main__':
    main()
