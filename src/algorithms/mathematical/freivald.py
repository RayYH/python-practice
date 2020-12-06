"""
Generate an n × 1 random 0/1 vector r.
Compute P = A × (Br) – Cr.
Return true if P = ( 0, 0, …, 0 )^T, return false otherwise.
"""
import random


def multi(m, v):
    n = len(m)
    return [sum(m[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivald(a, b, c):
    n = len(a)
    # generate random vector
    r = [random.randint(0, 1000000) for _ in range(n)]
    return multi(a, multi(b, r)) == multi(c, r)


def main():
    a = [[1, 1], [1, 1]]
    b = [[1, 1], [1, 1]]
    c = [[2, 2], [2, 2]]
    print(freivald(a, b, c))


if __name__ == '__main__':
    main()
