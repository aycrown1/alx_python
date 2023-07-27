#!/usr/bin/python3
def pow(a, b):
        result = 1
    
        # If b is negative, invert a and make b positive
        if b < 0:
            a = 1 / a
            b = -b
    
        # Calculate a^b by multiplying 'a' 'b' times
        for _ in range(b):
            result *= a
    
        return result