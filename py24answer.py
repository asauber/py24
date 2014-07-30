#!/usr/bin/env python
# 24 Game
# Copyright (C) Andrew Sauber 2014, All rights reserved
"""Enter four digits from 1 to 9.
The answer for the game "24" using those digits will be printed in prefix form.
Press C-c to exit."""

from __future__ import print_function
from itertools import permutations
import operator as ops
op = {
    '+' : ops.add,
    '-' : ops.sub,
    '*' : ops.mul,
    '/' : ops.div
}
try:
    input = raw_input
except NameError:
    pass

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

    # the answer is valid
    return inp

def get_valid_input():
    inp = ""
    while inp == "":
        inp = input("Input: ")
        try:
            inp = sanitize_input(inp)
        except ValueError:
            inp = ""

    return inp

def can_make_24(digits):
    Ns = permutations(digits)
    Ops = gen_ops_permutations()

    for ns in Ns:
        for ops in Ops:
            try:
                result = op[ops[0]](float(ns[1]), float(ns[0]))
                result = op[ops[1]](float(ns[2]), result)
                result = op[ops[2]](float(ns[3]), result)
                if abs(result - 24) < 0.01:
                    answer_string = "{} {} {} {} {} {} {}".format(
                                        ops[2], ns[3],
                                        ops[1], ns[2],
                                        ops[0], ns[1], ns[0])
                    return (True, answer_string)
            except ZeroDivisionError:
                continue
                

        for ops in Ops:
            try:
                result1 = op[ops[0]](float(ns[1]), float(ns[0]))
                result2 = op[ops[1]](float(ns[3]), float(ns[2]))
                result = op[ops[2]](result2, result1)
                if abs(result - 24) < 0.01:
                    answer_string = "{} {} {} {} {} {} {}".format(
                                        ops[2],
                                        ops[1], ns[3], ns[2],
                                        ops[0], ns[1], ns[0])
                    return (True, answer_string)
            except ZeroDivisionError:
                continue

    # none of the permutations were equal to 24
    return (False, "")

def gen_ops_permutations():
    return [(a + b + c) for a in "+-*/" for b in "+-*/" for c in "+-*/"]

def main():
    print_doc()
    while True:
        inp = get_valid_input()
        inp = [int(x) for x in list(inp)]
        (valid, answer_string) = can_make_24(inp)

        if valid:
            print("The way to make 24 is: ", answer_string)
        else:
            print("No way to make 24")
    
try:
    main()
except KeyboardInterrupt:
    print("\nThanks for using the 24 solver!")

