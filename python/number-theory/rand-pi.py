from math import gcd, sqrt
from random import randint


def rand_pi(samples=1000000, end=10000):
    coprime, cofactor = 0, 0
    for _ in range(samples):
        a = randint(1, end)
        b = randint(1, end)
        if gcd(a, b) == 1:
            coprime += 1
        else:
            cofactor += 1
    prob = coprime / (coprime + cofactor)
    return sqrt(6 / prob)

print(rand_pi())
