# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script builds a string created from the first characters of the words from the line,
and a string created from the last word characters from the line line - TASK 2.12.
"""

def first_chars_word(line):
    list_chars = line.split()
    result = ""
    index = 0
    for char in list_chars:
        result += char[0]
    return result


def last_chars_word(line):
    list_chars = line.split()
    result = ""
    for char in list_chars:
        result += char[-1]
    return result

def test_result():
    line = "Hello, my name is Sasha!"

    res1 = first_chars_word(line)
    res2 = last_chars_word(line)

    expected_res1 = "HmniS"
    expected_res2 = ",yes!"

    try:
        assert res1 == expected_res1
        assert res2 == expected_res2
        print("Word of first chars: {} \nWord of last chars: {}".format(res1, res2))
    except AssertionError:
        print("Tests failed")

    del line, res1, res2, expected_res1, expected_res2

def main():
    test_result()

if __name__ == "__main__":
    main()