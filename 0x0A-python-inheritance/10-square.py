#!/usr/bin/python3
"""This module conains a class called BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a Square and is
    child from Rectangle
    """

    def __init__(self, size):
        """This method initialize the class"""
        super().integer_validator("size", size)
        self._Square__size = size
        super().__init__(size, size)
