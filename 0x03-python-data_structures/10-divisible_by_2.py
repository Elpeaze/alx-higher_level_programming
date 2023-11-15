#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list


"""Alternative Solution
"""

""
def divisible_by_2(my_list=[]):
  _bool = []
  for value in my_list:
    if value % 2 == 0:
      _bool.append(True)
    else:
      _bool.append(False)
  return _bool
"""
