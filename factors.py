def prime_factors(n, k=2):
    """Returns the prime factorization of a natural number N."""
    if n == 1:
        return []
    elif n % k == 0:
        return [k] + prime_factors(n // k, k)
    return prime_factors(n, k + 1)

def print_pf(factors):
    """Prints the prime factorization from a list of factors."""
    factors_dict = {}
    for i in factors:
        if i not in factors_dict:
            factors_dict[i] = 1
        else:
            factors_dict[i] += 1
    factors_str = ''
    for p_factor, power in factors_dict.items():
        factors_str += '{0}^{1} * '.format(p_factor, power)
    return factors_str[:-3]

