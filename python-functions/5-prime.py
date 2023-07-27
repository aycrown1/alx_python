#!/usr/bin/python3
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True

    # Check for divisibility from 2 to the square root of the number (inclusive)
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
