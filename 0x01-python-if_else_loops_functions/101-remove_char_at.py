#!/usr/bin/env python3
def remove_char_at(str, n):
    ln = len(str)
    if n >= 0 and n <= ln:
        l = list(str)
        l[n] = ""
        str = "".join(l)
    return (str)
