#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.5

Script draws a "ruler" of a given length. Numbers consisting of several digits is handled in this way:
the last digit of the number is placed under the vertical line.
Firstly script builds a complete string, and then printa it.
"""

def print_measure(size):
    measure = "....".join("|" for i in range(size + 1))
    measure += "\n"

    space = " "; n = 4
    for i in range(size + 1):
        if len(str(i + 1)) - len(str(i)) == 1:
            n = 4 - len(str(i))
        measure += str(i) + "{}".format(space * n)

    print(measure)
    del measure, space, n

def main():
    size = 0
    try:
        size = int(input("Choose size of measure (int): "))
        print_measure(size)
    except ValueError:
        print("Error! 'int' type required")

    del size

if __name__ == '__main__':
    main()