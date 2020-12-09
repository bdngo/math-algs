"""Various sorts."""
from typing import List, TypeVar

T = TypeVar('T')

def insertion_sort(arr: List[T]) -> List[T]:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def selection_sort(arr: List[T]) -> List[T]:
    for i in range(len(arr)):
        argmin = arr.index(min(arr[i:]), i)
        arr[i], arr[argmin] = arr[argmin], arr[i]
    return arr


def merge_sort(arr: List[T]) -> List[T]:
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    def merge(a: List[T], b: List[T]) -> List[T]:
        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a
        if a[0] <= b[0]:
            return [a[0]] + merge(a[1:], b)
        return [b[0]] + merge(a, b[1:])
    half = len(arr) // 2
    return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))


def quick_sort(arr: List[T]) -> List[T]:
    if len(arr) == 0:
        return []
    head, tail = arr[0], arr[1:]
    return quick_sort(list(filter(lambda x: x <= head, tail))) + [head] + quick_sort(list(filter(lambda x: x > head, tail)))


def lsd_sort(arr: List[T]) -> List[T]:
    mask = 1
    while mask < (1 << 30):
        bins = {i: [] for i in range(10)}
        for j in arr:
            bins[j // mask % 10].append(j)
        arr = []
        for k in bins.values():
            arr.extend(k)
        mask *= 10
    return arr


def main() -> None:
    arr = [1, 4, 2, 6, 7, 2, 4, 10, 8, 2, 3, 3]
    print(lsd_sort(arr))


if __name__ == "__main__":
    main()
