#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    for i in reversed(range(length)):
        print("{}".format(my_list[i]))
