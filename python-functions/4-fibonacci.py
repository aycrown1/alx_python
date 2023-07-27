#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_numbers = [0, 1]
    for i in range(2, n):
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_fib)

    return fib_numbers