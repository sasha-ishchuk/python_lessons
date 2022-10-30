#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_measure(size):
    measure = "....".join("|" for i in range(size + 1))
    measure += "\n"
    space = " ";
    n = 4
    for i in range(size + 1):
        if len(str(i + 1)) - len(str(i)) == 1:
            n = 4 - len(str(i))
        measure += str(i) + "{}".format(space * n)
    return measure


def get_rect(width, height):
    rectangle_horizontal = "---".join("+" for i in range(width + 1))
    rectangle_vertical = "   ".join("|" for i in range(width + 1))
    rectangle = ""
    for i in range(height + 1):
        if i == height:
            rectangle += rectangle_horizontal
        else:
            rectangle += rectangle_horizontal + "\n" + rectangle_vertical + "\n"
    return rectangle


def main():
    print(get_measure(21))
    print(get_rect(4, 3))


if __name__ == '__main__':
    main()
