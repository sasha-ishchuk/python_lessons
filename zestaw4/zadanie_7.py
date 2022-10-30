#!/usr/bin/python
# -*- coding: utf-8 -*-

def flatten(sequence):
    result = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += flatten(i)
        else:
            result.append(i)
    return result


def main():
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(flatten(sequence))    # [1,2,3,4,5,6,7,8,9]


if __name__ == '__main__':
    main()