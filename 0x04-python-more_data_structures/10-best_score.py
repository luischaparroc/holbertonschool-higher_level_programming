#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    list_keys = list(a_dictionary.keys())
    name = list_keys[0]
    score = a_dictionary[list_keys[0]]

    for i in list_keys:
        if a_dictionary.get(i) >= score:
            name = i
            score = a_dictionary.get(i)

    return (name)
