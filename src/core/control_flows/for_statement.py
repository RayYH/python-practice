from math import sqrt


def sum_of_numbers(numbers):
    """
    Program to find the sum of all numbers stored in a list
    """
    # variable to store the sum
    sum_num = 0
    # iterate over the list
    for val in numbers:
        sum_num += val
    return sum_num


def frac(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def is_prime(num):
    num = abs(int(num))
    if num == 1 or num == 0:
        return False
    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True


def get_gcd_and_lcm(a, b):
    x = abs(int(a))
    y = abs(int(b))
    if x * y == 0:
        raise ValueError("Provided value cannot be zero")
    # make sure x is the lower one
    if x > y:
        x, y = y, x
    gcd, lcm = 1, x * y
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            gcd, lcm = factor, x * y // factor
            break
    return {'gcd': gcd, 'lcm': lcm}
