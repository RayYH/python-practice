def for_loop():
    # Program to find the sum of all numbers stored in a list
    # List of numbers
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
    # variable to store the sum
    sum_num = 0
    # iterate over the list
    for val in numbers:
        sum_num = sum_num + val
    print("The sum is", sum_num)


def range_usage():
    print(range(10))
    print(list(range(10)))
    print(list(range(2, 8)))
    print(list(range(2, 20, 3)))
    genre = ['pop', 'rock', 'jazz']
    # iterate over the list using index
    for i in range(len(genre)):
        print("I like", genre[i])


def for_loop_with_else():
    digits = [0, 1, 5]
    for i in digits:
        print(i)
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
    for_loop()
    range_usage()
    for_loop_with_else()


if __name__ == '__main__':
    main()
