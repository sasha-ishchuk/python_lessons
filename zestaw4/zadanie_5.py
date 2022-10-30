#!/usr/bin/python
# -*- coding: utf-8 -*-

def reverse_it(L, left, right):
    L[left:right + 1] = L[left:right + 1][::-1]
    return L


def reverse_rec(L, left, right):
    if left >= right:
        return L
    L[left], L[right] = L[right], L[left]
    return reverse_rec(L, left + 1, right - 1)


def main():
    lst1 = [10, 11, 12, 13, 14, 15]
    lst2 = [0, 1, 2, 3, 4, 5]
    print(reverse_it(lst1, 1, 4))    # 10 14 13 12 11 15
    print(reverse_rec(lst2, 1, 4))   # 0 4 3 2 1 5


if __name__ == '__main__':
    main()
