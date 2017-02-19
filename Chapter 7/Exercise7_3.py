"""
Write a function named test_square_root that prints a table.
The first column is a number, a; the second column is the square root of a computed with the function
from Exercise 7.2; the third column is the square root computed by math.sqrt; the fourth column
is the absolute value of the difference between the two estimates.
"""


def test_square_root(a):
    for num in range(1, a):
        x = num
        print(x)
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    print(num, x)


test_square_root(10)
print('done')
