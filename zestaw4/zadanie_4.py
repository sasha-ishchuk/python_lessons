#!/usr/bin/python
# -*- coding: utf-8 -*-

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


def main():
    print(fibonacci(8))


if __name__ == '__main__':
    main()
