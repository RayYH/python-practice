def break_usage():
    for val in "string":
        if val == "i":
            break
        print(val)
    print("The end")


def continue_usage():
    for val in "string":
        if val == "i":
            continue
        print(val)
    print("The end")


def main():
    break_usage()
    continue_usage()


if __name__ == '__main__':
    main()
