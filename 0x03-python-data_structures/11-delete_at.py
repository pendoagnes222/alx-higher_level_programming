#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if my_list:
        new_list = my_list[:]
        my_list.clear()
        for x in range(0, idx):
            my_list.append(new_list[x])
        for x in range(idx+1, len(new_list)):
            my_list.append(new_list[x])
        return my_list
    return my_list
