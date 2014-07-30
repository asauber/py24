#!/usr/bin/env python
# "24" Game Solver
# Copyright (C) Andrew Sauber 2014, All rights reserved
"""Enter four digits from 1 to 9, optionally seperated by whitespace only.
Example: 9 1 5 8
The answer for the game "24" using these digits will be printed in prefix form.
Press <ctrl>+c to exit."""

from __future__ import print_function
import py24util

def print_doc():
    print(__doc__)

def sanitize_input(inp):
    # remove all whitespace by taking advantage of split()
    inp = ''.join(inp.split())

    # input is invalid if it does not contain exactly 4 chars
    if len(inp) != 4:
        print("Your input must contain exactly 4 digits")
        raise ValueError

    # all of the chars must be digits in the range 1 through 9
    valid_chars_string = "123456789"
    for c in inp:
        if c not in valid_chars_string:
            print("Your input contains an invalid digit")
            raise ValueError

    # the input is valid
    return inp

def main():
    print_doc()
    while True:
        inp = py24util.get_valid_input("Input: ", sanitize_input)
        inp = [int(x) for x in list(inp)]
        (valid, answer_string) = py24util.can_make_24(inp)

        if valid:
            print("One way to make 24 is:", answer_string)
        else:
            print("No way to make 24")
    
try:
    main()
except KeyboardInterrupt:
    print("\nThanks for using the 24 solver!")

