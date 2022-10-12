# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script calculates the number of words in the text.
'Word' is a sequence of "black" characters, separated
from other words by whitespace (space, tab, newline) - TASK 2.10.
"""

def count_chars(text):
    chars_num = len(text.split())
    return chars_num

def first_test():
    example_text1 = "Hello, my name is Sasha!\n\tI'm studing computer science"
    res1 = count_chars(example_text1)
    expected_res1 = 9

    try:
        assert res1 == expected_res1
        print("Text: {}".format(example_text1))
        print("Number of words in text: {}".format(res1))
    except AssertionError:
        print("Tests failed")

    del example_text1, res1, expected_res1

def second_test():
    example_text2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Suspendisse fringilla orci eget felis vestibulum, ut feugiat purus semper.
            Ut pharetra aliquet leo. Maecenas dignissim ultricies eros vitae condimentum. 
            Curabitur tempus, dui vehicula accumsan."""
    res2 = count_chars(example_text2)
    expected_res2 = 33

    try:
        assert res2 == expected_res2
        print("\nText: {}".format(example_text2))
        print("Number of words in text: {}".format(count_chars(example_text2)))
    except AssertionError:
        print("Tests failed")

    del example_text2, res2, expected_res2

def main():
    first_test()
    second_test()

if __name__ == "__main__":
    main()