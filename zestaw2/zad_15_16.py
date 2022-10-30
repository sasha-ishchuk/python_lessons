# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script creates a string which is a sequence
of digits of consecutive numbers from the list L - TASK 2.15.

Script replace the string "GvR" with "Guido van Rossum" in the text - TASK 2.16.
"""

def get_string(my_list):
    result = "".join(str(x) for x in my_list)
    return result

def replace_string(text, old_string, new_string):
    result = text.replace(old_string, new_string)
    return result

def first_test():
    example_list = [1, 4, 23, 19, 0, 11, 87]
    res1 = get_string(example_list)
    expected_res1 = "14231901187"

    try:
        assert res1 == expected_res1
        print("List: {}".format(example_list))
        print("String sequence: {}".format(res1))
    except AssertionError:
        print("Tests failed")

    del example_list, res1, expected_res1

def second_test():
    line = """GvR is a Dutch programmer. GvR is best known as the creator 
                of the Python programming language. GvR  was born and raised in the Netherlands, 
                where GvR received a master's degree in mathematics and computer science."""
    res2 = replace_string(line, "GvR", "Guido van Rossum")
    expected_res2 = """Guido van Rossum is a Dutch programmer. Guido van Rossum is best known as the creator 
                of the Python programming language. Guido van Rossum  was born and raised in the Netherlands, 
                where Guido van Rossum received a master's degree in mathematics and computer science."""

    try:
        assert res2 == expected_res2
        print("\nText: {}".format(line))
        print("\nFormat text: {}".format(res2))
    except AssertionError:
        print("Tests failed")

    del line, res2, expected_res2

def main():
    first_test()
    second_test()

if __name__ == "__main__":
    main()