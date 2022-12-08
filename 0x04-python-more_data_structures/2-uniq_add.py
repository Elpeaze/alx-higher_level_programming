#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_set = set()

    for i in my_list:
        unique_set.add(i)

    return sum(unique_set)

