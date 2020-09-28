def greater_than_3(number):
    if number > 3:
        return True
    return False


def greater_than_5(number):
    if number > 5:
        return True
    else:
        return False


def equals(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def compare_to_zero(number):
    if number >= 0:
        if number == 0:
            return 0
        else:
            return 1
    else:
        return -1
