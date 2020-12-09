from typing import Callable, Tuple

f = lambda x: x**2
g = lambda x: 3*x - 2
func = lambda x: f(x) - g(x)
init_interval = (1.5, 10.) # pick sufficiently small interval

def sgn(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

def find_zeroes(function: Callable[[float], float], interval: Tuple[float], threshold: float) -> float:
    """Solves for the intersection of 2 single-variable functions."""
    zero, threshold = 0, 100
    left, right = interval[0], interval[1]
    while abs(function(zero)) > threshold:
        midpoint = (left + right) / 2
        left_bound, right_bound, mid_bound = function(left), function(right), function(midpoint)
        if sgn(left_bound) != sgn(mid_bound):
            right, zero = midpoint, midpoint
        elif sgn(right_bound) != sgn(mid_bound):
            left, zero = midpoint, midpoint
    return zero
