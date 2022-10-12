#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.6

Script draws a rectangle consisting of small squares.
Firstly script builds a complete string, and then print it.
"""

def print_rect(width, height):
    rectangle_horizontal = "---".join("+" for i in range(width + 1))
    rectangle_vertical = "   ".join("|" for i in range(width + 1))
    rectangle = ""
    for i in range(height + 1):
        if i == height:
            rectangle += rectangle_horizontal
        else:
            rectangle += rectangle_horizontal + "\n" + rectangle_vertical + "\n"
    print(rectangle)

    del rectangle_horizontal, rectangle_vertical, rectangle

def main():
    width, height = 0, 0
    try:
        width = int(input("Choose width of rectangle (int): "))
        height = int(input("Choose height of rectangle (int): "))
        print_rect(width, height)
    except ValueError:
        print("Error! 'int' type required")

    del width, height

if __name__ == '__main__':
    main()