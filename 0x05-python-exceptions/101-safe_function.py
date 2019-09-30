#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except ZeroDivisionError:
        sys.stderr.write("Exception: division by zero\n")
        result = None
    except IndexError:
        sys.stderr.write("Exception: list index out of range\n")
        result = None

    return (result)
