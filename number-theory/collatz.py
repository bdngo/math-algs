from typing import List

def collatz(n: int) -> List[int]:
    """Prints the Collatz sequence for a positive integer N."""
    if n == 1:
        return [1]
    return [n] + (collatz(n // 2) if n % 2 == 0 else collatz(3*n + 1))
