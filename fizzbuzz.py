def fizzbuzz(n):
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
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

