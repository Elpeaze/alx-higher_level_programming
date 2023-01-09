#!/usr/bin/python3
"""This module conains a class called BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Imports a class from another file"""


class Rectangle(BaseGeometry):
    """This is child class that defines a
    Rectangle
    """

    def __init__(self, width, height):
        """This method initialize the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height
