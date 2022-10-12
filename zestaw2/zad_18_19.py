# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script finds the number of digits zero in a large integer - TASK 2.18.

In the list L we have one-, two- and three-digit positive numbers.
Script builds a string from three-digit blocks, where one- and two-digit numbers has a block
padded with zeros (e.g. 007, 024) - TASK 2.19.
"""

def count_zeros(number):
    result = str(number).count("0")
    return result

def format_digits(my_list):
    result = " ".join(str(my_list[i]).zfill(3) for i in range(0, len(my_list), 1))
    return result

def first_test():
    a = 1020305550008064003
    b = 30004502709070002103000230
    c = 2000540070100002300405060700010020300400

    res1 = count_zeros(a)
    expected_res1 = 9

    res2 = count_zeros(b)
    expected_res2 = 14

    res3 = count_zeros(c)
    expected_res3 = 25

    try:
        assert res1 == expected_res1
        print("Integer: {} (number of zeros: {})".format(a, res1))

        assert res2 == expected_res2
        print("Integer: {} (number of zeros: {})".format(b, res2))

        assert res3 == expected_res3
        print("Integer: {} (number of zeros: {})".format(c, res3))

    except AssertionError:
        print("Tests failed")

    del a, b, c
    del res1, res2, res3
    del expected_res1, expected_res2, expected_res3

def second_test():
    first_list = [1, 32, 2, 390, 43, 233, 4, 6, 87]
    second_list = [2, 87, 9, 234, 564, 1, 9, 872, 13, 6, 131, 2, 7, 38, 21, 8]

    res1 = format_digits(first_list)
    expected_res1 = "001 032 002 390 043 233 004 006 087"

    res2 = format_digits(second_list)
    expected_res2 = "002 087 009 234 564 001 009 872 013 006 131 002 007 038 021 008"

    try:
        assert res1 == expected_res1
        print("\nList: {} \nResult string: {}".format(first_list, res1))

        assert res2 == expected_res2
        print("\nList: {} \nResult string: {}".format(second_list, res2))

    except AssertionError:
        print("Tests failed")

def main():
    first_test()
    second_test()

if __name__ == "__main__":
    main()