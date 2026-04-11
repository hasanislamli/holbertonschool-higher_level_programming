#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Square class with size validation and printing method"""

    def __init__(self, size=0):
        """Initialize square with validated size"""
        self.size = size

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area"""
        return self.__size ** 2

    def my_print(self):
        """Print square using #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
