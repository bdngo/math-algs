from typing import List

def digit_root(n: int, base: int=10) -> int:
    """Returns the digital root for an integer N."""
    assert type(n) == 'int'
    total = 0
    while n:
        total += n % base
        n //= base
    return digit_root(total) if total >= base else total

def int_to_list(n: int, base: int=10) -> List[int]:
    """Returns a list of the digits of N."""
    digit_list = []
    while n:
        digit_list += [n % base]
        n //= base
    return list(reversed(digit_list))

def check_sum(n: int) -> bool:
    """Checks if N is a valid bank card."""
    digits, doubled_digits = int_to_list(n), []
    for i in range(len(digits)):
        doubled_digits.append(
            digit_root(digits[i] * 2) if i % 2 == 0 else digits[i])
    return sum(doubled_digits) % 10 == 0

def vat_check(n: int) -> bool:
    """Checks if N satisfies the old HMRC VAT number check."""
    factor = 8
    digits, last_two = int_to_list(n)[:-2], int_to_list(n)[-2:]
    for i in range(len(digits)):
        digits[i] *= factor
        factor -= 1
    check_digit = sum(digits) + (last_two[0]*10 + last_two[1]) + 55
    return check_digit % 97 == 0
