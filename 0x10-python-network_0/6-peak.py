#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    mid = int(length / 2)
    li = list_of_integers
    if mid - 1 < 0 or mid + 1 >= length:
        return li[mid]
    if li[mid - 1] < li[mid] > li[mid + 1]:
        return li[mid]
    high = find_peak(li[mid:])
    low = find_peak(li[:mid])
    return high if high > low else low
