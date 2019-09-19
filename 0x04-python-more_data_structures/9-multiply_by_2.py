#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    if a_dictionary is None:
        return

    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        if new_dir.get(i) % 2 == 0:
            new_dir[i] *= 2

    return (new_dir)
