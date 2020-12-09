def fizzbuzz(n: int) -> None:
    """Solves the FizzBuzz problem.

    >>> fizzbuzz(10)
    1
    2
    fizz
    4
    buzz
    6
    7
    8
    fizz
    buzz
    """
    for i in range(1, n + 1):
        s = ''
        if i % 3 == 0:
            s += 'fizz'
        if i % 5 == 0:
            s += 'fuzz'
        if s == '':
            s += str(i)
        print(s)
