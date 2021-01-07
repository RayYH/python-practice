from random import randint


def multi(m, v):
    n = len(m)
    return [sum(m[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivald(a, b, c):
    """
    Freivalds' algorithm

    Generate an n × 1 random 0/1 vector r.
    Compute P = A × (Br) – Cr.
    Return true if P = ( 0, 0, …, 0 )^T, return false otherwise.
    """
    n = len(a)
    # generate random vector
    r = [randint(0, 1000000) for _ in range(n)]
    # abr=cr means ab=c
    return multi(a, multi(b, r)) == multi(c, r)
