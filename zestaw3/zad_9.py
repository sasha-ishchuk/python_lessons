#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.9

We have a given list of sequences (lists or tuples) of various lengths containing numbers.
Script finds a list that contains the sums of the numbers in these sequences.
"""

def get_sum_list(list_elements):
    result_list = []
    for item in list_elements:
        result_list.append(sum(item))
    return result_list

def test_result():
    list_of_lists = [[], [3, 2, 10], (2, 3), [8, 0, 7, 2, 5, 1, 0, 2],
                     (13, 2), [], [1, 0, 2, 9, 3, 8, 6], [5, 8, 11, 23]]
    print("List of lists: {}".format(list_of_lists))

    res = get_sum_list(list_of_lists)
    expected_res = [0, 15, 5, 25, 15, 0, 29, 47]

    try:
        assert res == expected_res
        print("Sum of elements in each list: {}".format(res))
    except AssertionError:
        print("Tests failed")

    del list_of_lists, res, expected_res

def main():
    test_result()

if __name__ == '__main__':
    main()