Python Exceptions - Safe List Printing

Project Overview
This project focuses on learning Python exception handling. The goal is to safely print elements from a list without causing runtime errors when accessing out-of-range indexes.

File
0-safe_print_list.py

Task Description
Write a function:
def safe_print_list(my_list=[], x=0):

Requirements:

* Print x elements from my_list
* Print all elements on the same line
* End output with a new line
* x can be greater than the size of the list
* Use try/except
* Do not use len()
* Do not import any module

Function Behavior
The function iterates up to x elements and attempts to print each one. If an index does not exist in the list, it handles the exception and stops printing. It returns the number of elements actually printed.

Example
my_list = [1, 2, 3, 4, 5]

safe_print_list(my_list, 2)
Output: 12

safe_print_list(my_list, 10)
Output: 12345

Return Value
The function returns an integer representing the number of elements successfully printed.

Key Concepts

* Exception handling (try/except)
* Safe list access
* Preventing runtime errors

Constraints

* No use of len()
* No imports allowed
* Must handle exceptions properly

Learning Objective
The purpose of this task is to understand how to write safe and robust Python code using exception handling.

