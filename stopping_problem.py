from math import e, sqrt
from random import sample
from typing import Callable, Tuple, Union

candidates = range(10000)

def stopping_problem(lst: Union[int, float],
                        f: Callable[[Union[int, float]], float]=lambda x: x) -> Tuple[float, int]:
    """Returns the optimal element of LST according to F paradigm. Default F is identity.
    Use square root for most efficient runtime, or use 1/e for best candidate."""
    lst = sample(lst, len(lst))
    pivot = int(f(len(lst)))
    benchmark, runs = max(lst[:pivot]), len(lst[:pivot])
    for i in lst[pivot:]:
        runs += 1
        if i > benchmark:
            return i, runs
    return benchmark, runs

sp_sqrt = [stopping_problem(candidates, lambda x: sqrt(x)) for _ in range(100)]
sp_e = [stopping_problem(candidates, lambda x: x / e) for _ in range(100)]

print(min(sp_sqrt, key=lambda x: x[1]))
print(min(sp_e, key=lambda x: x[1]))

