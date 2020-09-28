def sum_from_1_to_n(n):
    num_sum = 0
    i = 1
    while i <= n:
        num_sum = num_sum + i
        i = i + 1
    return num_sum


def while_loop_with_else():
    counter = 0
    while counter < 3:
        print("Inside loop", end=" ")
        counter = counter + 1
    else:
        print("Inside else", end=" ")
