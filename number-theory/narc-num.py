from typing import List


def int_to_list(n: int, base: int=10) -> List[int]:
    """Returns a list of the digits of N."""
    digit_list = []
    while n:
        digit_list += [n % base]
        n //= base
    return list(reversed(digit_list))

def narc(n: int) -> int:
    """Raises the digits of an integer N to the power of the number of digits."""
    digits = int_to_list(n)
    return sum(map(lambda x: x**len(digits), digits))

def narc_num(n: int) -> bool:
    """Determines if an integer N is a narcissistic number."""
    return narc(n) == n

def narc_cycle(n: int) -> Tuple(int, int):
    curr_narc = narc(n)
    path = [n]
    while curr_narc != n:
        path += [curr_narc]
        curr_narc = narc(curr_narc)
    return path, len(path)
