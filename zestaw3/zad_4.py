#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TASK 3.4

Script asks user for the real number x (float type) in loop and printing x and the third power of x.
Script is stopped by typing stop. If the user enters the string instead of a number,
the script is printing an error message and continue working.
"""
import sys

def main():
    while True:
        answer = input("Type a float number ['stop' to exit]: ")
        if answer == "stop":
            del answer
            sys.exit()
        try:
            answer = float(answer)
            print("Your number is {}, third power of number is {}".format(float(answer), pow(float(answer), 3)))
        except ValueError:
            print("Error! Number required.")

if __name__ == "__main__":
    main()