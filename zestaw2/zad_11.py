# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script displays word in way that its characters are separated by an underscore - TASK 2.11.
"""

def change_text(text):
    result = '_'.join(text)
    return result

def test_result():
    text = "word"
    print("Text: {}".format(text))

    res = change_text(text)
    expected_res = "w_o_r_d"

    try:
        assert res == expected_res
        print("Changed text: {}".format(res))
    except AssertionError:
        print("Tests failed")

    del text, res, expected_res

def main():
    test_result()

if __name__ == "__main__":
    main()