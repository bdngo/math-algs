from random import sample

names = ['Alfred', 'Bryan', 'Harsh', 'Leo', 'Stanley']

def draw_lots(name_lst):
    """Draws lots from NAME_LST, prints each result."""
    new_names = []
    for i in sample(range(len(name_lst)), len(name_lst)):
        print(name_lst[i])
        new_names.append(name_lst[i])
    return new_names

new_names = draw_lots(names)

def bogo_sort(condition):
    """Sorts the list repeatedly until CONDITION is met. Returns number of RUNS required."""
    global names, new_names
    runs = 0
    while not condition():
        new_names = draw_lots(names)
        runs += 1
    else:
        print(runs)
        return runs

# bogo_sort(lambda: new_names == names)
