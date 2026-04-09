#!/usr/bin/python3

f = __import__('add_0')

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, f.add(a, b)))
