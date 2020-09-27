from src.helper.line import dash


@dash
def break_usage():
    for letter in "string":
        if letter == "i":
            break
        print(letter)


@dash
def continue_usage():
    for letter in "string":
        if letter == "i":
            continue
        print(letter)


def main():
    print("\nBreak Usage:")
    break_usage()
    print("\nContinue Usage:")
    continue_usage()


if __name__ == '__main__':
    main()
