def while_loop():
    num_sum = 0
    n = 10
    i = 1
    while i <= n:
        num_sum = num_sum + i
        i = i + 1
    print("The sum is", num_sum)


def while_loop_with_else():
    counter = 0
    while counter < 3:
        print("Inside loop")
        counter = counter + 1
    else:
        print("Inside else")


def main():
    while_loop()
    while_loop_with_else()


if __name__ == '__main__':
    main()
