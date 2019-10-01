#!/usr/bin/python3
class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
            return

        self.__size = size
        self.__position = position

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
            return

        self.__position = value
