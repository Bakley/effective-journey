import math
"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b.
"""


def is_power(a, b):
    if a % b == 0 and a / b == math.pow(b, a):
        print(True)
    else:
        print(False)

        
is_power(2, 4)
