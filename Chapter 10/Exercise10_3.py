"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the comparison operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should re-
turn False.
"""


def is_sorted(x):
    for element in x:
        print(x)
        if element in x is sorted(element):
            return True
        else:
            return False
    return x

is_sorted([1, 2, 2])
