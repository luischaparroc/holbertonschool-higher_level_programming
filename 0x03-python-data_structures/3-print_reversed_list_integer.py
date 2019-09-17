#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list == []:
        pass
    else:
        length = len(my_list)
        for i in reversed(range(length)):
            print("{:d}".format(my_list[i]))
