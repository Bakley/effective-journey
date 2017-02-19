# coding=utf-8
# Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.


def is_between(x, y, z):
    if x < y < z:
        return True
    else:
        return False


print(is_between(1, 2, 3))
print(is_between(3, 2, 1))
print(is_between(5, 5, 5))
