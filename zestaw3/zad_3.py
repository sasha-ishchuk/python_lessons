#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.3
Script prints numbers from 0 to 30 except numbers that are divisible by 3.
"""

def main():
    for x in range(0, 30, 1):
        if not x % 3 == 0:
            print(x, end=" ")

if __name__ == "__main__":
    main()