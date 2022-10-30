#!/usr/bin/python
# -*- coding: utf-8 -*-

def sum_seq(sequence):
    total = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            total += sum_seq(i)
        else:
            total += i
    return total


def main():
    sequence = [1, 2, 1, (0, 5), 6, [5, 1, (3, 6), 8], 2]
    print(sum_seq(sequence))  # 40


if __name__ == '__main__':
    main()
