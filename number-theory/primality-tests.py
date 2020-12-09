from typing import Generator

def trial_div(n: int) -> bool:
    """Determines if natural number N is prime by trial division."""
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def lucas_lehmer() -> Generator[int, None, None]:
    """Generates the Lucas-Lehmer sequence."""
    seed = 4
    while True:
        yield seed
        seed = seed**2 - 2


def ll_primality(n: int) -> bool:
    """Determines if Mersenne number 2^N - 1 is prime via the Lucas-Lehmer primality test."""
    if n <= 2 or not trial_div(n):
        return False
    luc_leh = lucas_lehmer()
    for _ in range(n - 1):
        ll = next(luc_leh)
    return ll % (2**n - 1) == 0


def sieve(n: int) -> Generator[int, None, None]:
    """Yields all primes below N using the Sieve of Eratosthenes."""
    primes, p = [i for i in range(2, n + 1)], 2
    while p**2 < n:
        for i in primes:
            if i % p == 0 and i != p:
                primes.remove(i)
        p += 1
    yield from primes
