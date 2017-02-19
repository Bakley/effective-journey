from __future__ import unicode_literals

lis = [1, 2, 3, 4]


def add_list(n):
    cumulative_list = []
    total = 0
    for x in n:
        total += x
        print(total)
        cumulative_list.append(total)
    print(cumulative_list)
    
    
add_list(lis)
