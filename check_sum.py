def digit_root(n, base=10):
    """Returns the digital root for an integer N."""
    assert type(n) == 'int'
    total = 0
    while n:
        total += n % base
        n //= base
    if total >= base:
        return digit_root(total)
    return total

def int_to_list(n, base=10):
    """Returns a list of the digits of N."""
    digit_list = []
    while n:
        digit_list += [n % base]
        n //= base
    return list(reversed(digit_list))

def check_sum(n):
    """Checks if N is a valid bank card."""
    digits, doubled_digits = int_to_list(n), []
    for i in range(len(digits)):
        if i % 2 == 0:
            doubled_digits.append(digit_root(digits[i] * 2))
        else:
            doubled_digits.append(digits[i])
    if sum(doubled_digits) % 10 == 0:
        return True
    return False

def vat_check(n):
    """Checks if N satisfies the old HMRC VAT number check."""
    factor = 8
    digits, last_two = int_to_list(n)[:-2], int_to_list(n)[-2:]
    for i in range(len(digits)):
        digits[i] *= factor
        factor -= 1
    check_digit = sum(digits) + (last_two[0]*10 + last_two[1]) + 55
    if check_digit % 97 == 0:
        return True
    return False

