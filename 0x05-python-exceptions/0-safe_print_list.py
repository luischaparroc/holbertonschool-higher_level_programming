#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:
        print()
        return (0)

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except:
            i -= 1
            break

    print()
    return (i + 1)
