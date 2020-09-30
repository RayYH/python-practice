def sum_from_1_to_n(n):
    num_sum = 0
    i = 1
    while i <= n:
        # The ++ operator is not available in Python.
        num_sum += i
        i += 1
    return num_sum


def while_loop_with_else():
    counter = 0
    while counter < 3:
        print("Inside loop", end=" ")
        counter += 1
    else:
        print("Inside else", end=" ")
