#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Constructor """
        self.size = size

    @property
    def size(self):
        """ Getter """
        return self.__size


    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

