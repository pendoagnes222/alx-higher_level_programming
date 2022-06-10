#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    m = sorted(a_dictionary)
    for i in m:
        print("{:s}: {}".format(i, a_dictionary[i]))
