#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.10

Script creates a dictionary that translates numbers written in the Roman system
(with the letters I, V, X, L, C, D, M) into Arabic numbers
(script provides several ways to create such a dictionary).

roman2int_ver1() and roman2int_ver2 functions translate given Roman digitinto Arabic
using get_roman_verion1() and get_roman_verion2() dictionaries appropriately.
"""

def get_roman_version1():
    dictionary = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
    return dictionary

def get_roman_version2():
    dictionary = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)]
    return dictionary

def roman2int_ver1(roman_number):
    dictionary = get_roman_version1()
    int_val = 0
    for i in range(len(roman_number)):
        if i > 0 and dictionary[roman_number[i]] > dictionary[roman_number[i - 1]]:
            int_val += dictionary[roman_number[i]] - 2 * dictionary[roman_number[i - 1]]
        else:
            int_val += dictionary[roman_number[i]]
    return int_val

def roman2int_ver2(roman_number):
    dictionary = get_roman_version2()
    x, y, result = 0, 0, 0
    while x < len(roman_number):
        while y < len(dictionary) and not roman_number.startswith(dictionary[y][0], x):
            y += 1
        if y < len(dictionary):
            result += dictionary[y][1]
            x += len(dictionary[y][0])
        else:
            raise ValueError('Invalid Roman numeral')
    return result

def test_ver1():
    roman_num1 = "LXXIX"
    res1 = roman2int_ver1(roman_num1)
    expected_res1 = 79

    try:
        assert res1 == expected_res1
        print("Roman numeral: {} \nArabic number (ver1): {}".format(roman_num1, res1))
    except AssertionError:
        print("Tests failed")

    del roman_num1, res1, expected_res1

def test_ver2():
    roman_num2 = "XXIV"
    res2 = roman2int_ver2(roman_num2)
    expected_res2 = 24

    try:
        assert res2 == expected_res2
        print("\nRoman numeral: {} \nArabic number (ver2): {}".format(roman_num2, res2))
    except AssertionError:
        print("Tests failed")

    del roman_num2, res2, expected_res2

def main():
    test_ver1()
    test_ver2()

if __name__ == '__main__':
    main()