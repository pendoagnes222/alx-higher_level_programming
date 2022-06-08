#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    new_list = list(set(my_list))
    for item in new_list:
        y += item
    return y
