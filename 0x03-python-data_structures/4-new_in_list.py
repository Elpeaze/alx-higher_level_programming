#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy


"""
def new_in_list(my_list, idx. element):
    new_list = my_list.copy()
    if (idx < 0) or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list[idx] = element
        return new_list


def new_in_list(my_list, idx, element):
  new_list = my_list[:]
  if idx < 0 or idx >= len(my_list):
    return my_list[:]
  else:
    new_list[idx] = element
    return new_list
"""
