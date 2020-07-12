def if_statements():
    num = 3
    if num > 0:
        print(num, "is a positive number.")
    print("This is always printed.")

    num = -1
    if num > 0:
        print(num, "is a positive number.")
    print("This is also always printed.")


def if_else_statements():
    num = 3
    if num >= 0:
        print("Positive or Zero")
    else:
        print("Negative number")


def if_elif_else_statements():
    num = 3.4
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")


def nested_if_statements():
    num = float(input("Enter a number: "))
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")


def main():
    if_statements()
    if_else_statements()
    if_elif_else_statements()
    nested_if_statements()


if __name__ == '__main__':
    main()
