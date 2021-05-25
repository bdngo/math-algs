from random import uniform
from typing import Callable, Tuple, Type

def estimate_pi() -> float:
    """Approximates π."""
    samples, in_func = 1000, 0
    for _ in range(samples):
        rand_x, rand_y = uniform(-1, 1), uniform(-1, 1)
        if rand_x**2 + rand_y**2 <= 1:
            in_func += 1
    return 4 * (in_func / samples)

def monte_carlo_integration(f: Callable[[float], float], bounds: Tuple[float, float]):
    """Numerically integrates F between BOUNDS."""
    left, right = bounds[0], bounds[1]
    samples, integral = 1000000, 0.
    for _ in range(samples):
        rand_point = uniform(left, right)
        integral += f(rand_point)
    return (right - left) / samples * integral
