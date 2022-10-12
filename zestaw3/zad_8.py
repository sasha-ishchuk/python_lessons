#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.8

For two sequences of numbers script finds:
(a) a list of elements occurring in both sequences (no repetitions),
(b) a list of all elements from both sequences (no repetitions).
"""

def get_same_elements(first_sequence, second_sequence):
    first_set = set(first_sequence)
    second_set = set(second_sequence)
    if first_set & second_set:
        return sorted(first_set & second_set)

def get_all_elements(first_sequence, second_sequence):
    sequence = first_sequence + second_sequence
    return sorted(set(sequence))

def test_result():
    first_seq = (1, 54, 7, 10, 32, 26, 32, 3, 88)
    second_seq = (3, 43, 88, 111, 77, 12, 90, 1, 15)
    print("First sequence: {} \nSecond sequence: {}".format(first_seq, second_seq))

    expected_res1 = [1, 3, 88]
    expected_res2 = [1, 3, 7, 10, 12, 15, 26, 32, 43, 54, 77, 88, 90, 111]

    res1 = get_same_elements(first_seq, second_seq)
    res2 = get_all_elements(first_seq, second_seq)

    try:
        assert res1 == expected_res1
        print("\nElements occuring in both sequences: {}".format(res1))

        assert res2 == expected_res2
        print("All elements in sequences: {}".format(res2))
    except AssertionError:
        print("Tests failed")

    del first_seq, second_seq
    del res1, res2, expected_res1, expected_res2

def main():
    test_result()

if __name__ == '__main__':
    main()