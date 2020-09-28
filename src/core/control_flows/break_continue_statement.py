def break_usage():
    for letter in "string":
        if letter == "i":
            break
        print(letter, sep="", end="")


def continue_usage():
    for letter in "string":
        if letter == "r":
            continue
        print(letter, sep="", end="")
