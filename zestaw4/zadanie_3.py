#!/usr/bin/python
# -*- coding: utf-8 -*-

def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def main():
    print(factorial(4))


if __name__ == '__main__':
    main()
