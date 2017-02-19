"""
Write a function called chop that takes a list and modifies it, removing the first and
last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that contains all but the
first and last elements.
"""


def chop(x):
    new_list = []
    for element in range(2, len(x)):
        new_list.append(element)
        x = new_list.sort()
    print(new_list)
    return x





def middle(y):
    del y[1:len(elements)]


lis = [1, 2, 3, 4]
elements = [0, 9, 8, 7, 6]
print(chop(lis))
middle(elements)
print(elements)
