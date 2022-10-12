# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script finds the total length of the words in line (without whitespaces) - TASK 2.13.

Script finds the longest word and the length of the longest word in the string line - TASK 2.14.
"""

def words_len(line):
    res = sum(not chr.isspace() for chr in line)
    return res


def longest_word(line):
    line_list = line.split()
    sort_list = sorted(line_list, key=len)
    return sort_list[-1]

def first_test():
    line = "my favorite music style is techno"
    res1 = words_len(line)
    expected_res1 = 28

    try:
        assert res1 == expected_res1
        print("String: {}".format(line))
        print("\nLength of string: {}".format(len(line)))
        print("Length of all words in string: {}".format(res1))
    except AssertionError:
        print("Tests failed")

    del line, res1, expected_res1

def second_test():
    line = "my favorite music style is techno"
    res2 = longest_word(line)
    expected_res2 = "favorite"

    try:
        assert res2 == expected_res2
        print("\nThe longest word in string: {}".format(res2))
        print("Its length is: {}".format(len(res2)))
    except AssertionError:
        print("Tests failed")

    del line, res2, expected_res2

def main():
    first_test()
    second_test()

if __name__ == "__main__":
    main()