#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return

    if not value:
        return

    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
