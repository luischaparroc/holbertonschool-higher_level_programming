The ``1-my_list`` module
============================

Using ``MyList``
---------------------

Importing function from the module:
    >>> MyList = __import__('1-my_list').MyList


Printing a sorted list 1 (positive numbers)
    >>> my_list = MyList()
    >>> my_list += [0]
    >>> my_list.append(4)
    >>> my_list.append(1)
    >>> my_list.append(10)
    >>> my_list.append(3)
    >>> my_list.append(7)
    >>> my_list.print_sorted()
    [0, 1, 3, 4, 7, 10]


Printing a sorted list 2 (repeated numbers)
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list += [1]
    >>> my_list.append(2)
    >>> my_list.append(2)
    >>> my_list += [2]
    >>> my_list.print_sorted()
    [1, 1, 2, 2, 2]


Printing an sorted list 3 (one number)
    >>> my_list = MyList()
    >>> my_list += [3]
    >>> my_list.print_sorted()
    [3]


Printing an sorted list 4 (positive and negative numbers)
    >>> my_list = MyList()
    >>> my_list.append(-5)
    >>> my_list += [5]
    >>> my_list += [4]
    >>> my_list.append(0)
    >>> my_list.append(-4)
    >>> my_list.append(1)
    >>> my_list += [-1]
    >>> my_list.print_sorted()
    [-5, -4, -1, 0, 1, 4, 5]


Printing an empty list
    >>> my_list = MyList()
    >>> my_list.print_sorted()
    []


MyList is an instance of the class list
    >>> my_list = MyList()
    >>> isinstance(my_list, list)
    True


Instance has the correct type
    >>> my_list = MyList()
    >>> type(my_list) == MyList
    True


MyList is a subclass of list
    >>> issubclass(MyList, list)
    True


Print_sorted method with 1 passed argument
    >>> my_list = MyList()
    >>> my_list.print_sorted([1, 2, 3])
    Traceback (most recent call last):
    	      ...
    TypeError: print_sorted() takes 1 positional argument but 2 were given


Print_sorted method with 2 passed arguments
    >>> my_list = MyList()
    >>> my_list.print_sorted([1, 2], [5, 4])
    Traceback (most recent call last):
    	      ...
    TypeError: print_sorted() takes 1 positional argument but 3 were given


Type of the print_sorted method
    >>> my_list = MyList()
    >>> type(my_list.print_sorted)
    <class 'method'>


Check printable string
    >>> my_list = MyList()
    >>> my_list.append(5)
    >>> print(my_list)
    [5]

Check if print_sorted() returns a new list
    >>> my_list = MyList()
    >>> my_list.append(7)
    >>> my_list.append(1)
    >>> my_list.append(2)
    >>> my_list.print_sorted()
    [1, 2, 7]
    >>> my_list
    [7, 1, 2]
