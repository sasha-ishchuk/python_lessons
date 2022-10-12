# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script sorts the words in string once alphabetically, and once by its length - TASK 2.17.
"""

def sort_alphabetically(text):
    text_list = text.split()
    sort_list = sorted(text_list)
    result = " ".join(sort_list)
    return result

def sort_by_length(text):
    text_list = text.split()
    sort_list = sorted(text_list, key=len)
    result = " ".join(sort_list)
    return result

def test_result():
    text = "lorem ipsum dolor sit amet consectetur adipiscing elit fusce aliquam"
    print("Text: {}".format(text))

    res1 = sort_alphabetically(text)
    res2 = sort_by_length(text)

    expected_res1 = "adipiscing aliquam amet consectetur dolor elit fusce ipsum lorem sit"
    expected_res2 = "sit amet elit lorem ipsum dolor fusce aliquam adipiscing consectetur"

    try:
        assert res1 == expected_res1
        print("\nWords sorted alphabetically: {}".format(res1))

        assert res2 == expected_res2
        print("Words sorted by length: {}".format(res2))
    except AssertionError:
        print("Tests failed")

    del text, res1, res2, expected_res1, expected_res2

def main():
    test_result()

if __name__ == "__main__":
    main()