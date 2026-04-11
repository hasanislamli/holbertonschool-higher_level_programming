#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Square class with size validation and getter/setter"""

    def __init__(self, size=0):
        """Initialize square with validated size"""
        self.size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
