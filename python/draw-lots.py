from random import sample
from typing import Callable, List

NAMES = ['Alice', 'Bob', 'Charlie', 'Danielle', 'Emily']

def draw_lots(name_lst: List[str]) -> List[str]:
    """Draws lots from NAME_LST, prints each result."""
    new_names = []
    for i in sample(range(len(name_lst)), len(name_lst)):
        print(name_lst[i])
        new_names.append(name_lst[i])
    return new_names

new_names = draw_lots(NAMES)

def bogo_sort(condition: Callable[[List[str]], List[str]]) -> int:
    """Sorts the list repeatedly until CONDITION is met. Returns number of RUNS required."""
    global NAMES, new_names
    runs = 0
    while not condition():
        new_names = draw_lots(NAMES)
        runs += 1
    else:
        print(runs)
        return runs

# bogo_sort(lambda: new_names == names)
