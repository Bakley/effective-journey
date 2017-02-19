import math

"""
Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right
triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.
"""


def hypotenuse(x, y):
    base = x ** 2
    height = y ** 2
    hyp = base + height
    results = math.sqrt(hyp)
    return results


print(hypotenuse(3, 5))
print(hypotenuse(4, 5))
