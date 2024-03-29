from typing import List


def prime_factors(n: int, k: int=2) -> List[int]:
    """Returns the prime factorization of a natural number N."""
    if n == 1:
        return []
    elif n % k == 0:
        return [k] + prime_factors(n // k, k)
    return prime_factors(n, k + 1)

def print_pf(n: int) -> str:
    """Returns the (nicer) prime factorization of a natural number N."""
    factors_dict = {}
    for i in prime_factors(n):
        if i not in factors_dict:
            factors_dict[i] = 1
        else:
            factors_dict[i] += 1
    factors_str = ''
    for prime, power in factors_dict.items():
        factors_str += '{0}^{1} * '.format(prime, power)
    return factors_str[:-3]

def factors(n: int) -> List[int]:
    """Returns all the factors of an integer N."""
    return [i for i in range(1, n + 1) if n % i == 0]

def perfect_num(n: int) -> bool:
    """Determines if natural number N is a perfect number."""
    return sum(factors(n)[:-1]) == n
