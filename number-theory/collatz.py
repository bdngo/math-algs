def collatz(n):
    """Prints the Collatz sequence for a positive integer N."""
    if n == 1:
        return [1]
    if not n % 2: # N is even
        return [n] + collatz(n // 2)
    return [n] + collatz(3 * n + 1) # N is odd

