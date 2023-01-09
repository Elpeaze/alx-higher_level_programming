#!/usr/bin/python3
"""This module conains a class called BaseGeometry
"""


class BaseGeometry:
    """This class is the parent class of geometry"""

    def area(self):
        """this method defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This method is child class that defines a
    Rectangel
    """

    def __init__(self, width, height):
        """This method initialize the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method return the area"""
        return self.__width * self.__height

    def __str__(self):
        """This method is called when "print" or "str"
        is called
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """This class defines a Square and is
    child from Rectangle
    """

    def __init__(self, size):
        """This method initialize the class"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This method return the area"""
        return self.__size**2

    def __str__(self):
        """This method is called when "print" or "str"
        is called
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
