#!/usr/bin/env python
# 24 Game
# Copyright (C) Andrew Sauber 2014, All rights reserved
"""Four numbers will be shown, enter a prefix expression using the operators:
    add:       + x y
    subtract:  - x y
    multiply:  * x y
    divide:    / x y

Your expression must equal 24. For example, if you were given these numbers:
    1 6 2 8

You could enter:
    / * 6 8 * 2 1

Or if you were given these numbers:
    4 4 4 7

You could enter:
    * - 7 4 + 4 4

Press C-c to exit. Good Luck!"""

from __future__ import print_function
import random
import re
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

def print_rules():
    print(__doc__)

def gen_4_digits():
    return [random.randint(1,9) for x in xrange(4)]

def sanitize_answer(answer, digits):
    # remove all whitespace by taking advantage of split()
    answer = ''.join(answer.split())

    # answer is invalid if it does not contain exactly 7 chars
    if len(answer) != 7:
        print("Your answer must contain 3 operators and 4 digits")
        raise ValueError

    # all of the chars must be valid for the set of digits and operations
    valid_chars_string = str(''.join(str(d) for d in digits)) + "+-*/"
    for c in answer:
        if c not in valid_chars_string:
            print("Your answer contains an invalid number or operator")
            raise ValueError

    # the answer must take one of two prefix forms
    pattern1 = re.compile("[+\-*/][+\-*/]\d\d[+\-*/]\d\d") 
    pattern2 = re.compile("[+\-*/]\d[+\-*/]\d[+\-*/]\d\d")
    if not pattern1.match(answer) and not pattern2.match(answer):
        print("Your answer isn't in prefix notation")
        raise ValueError

    # the answer is valid
    return answer

def get_valid_answer(digits):
    answer = ""
    while answer == "":
        answer = input("Answer: ")
        try:
            answer = sanitize_answer(answer, digits)
        except ValueError:
            answer = ""
            continue

    return answer

def evaluate_answer(answer):
    stack = [ ]

    answer = list(answer)
    answer.reverse()
    try:
        for c in answer:
            if c not in op.keys():
                stack.append(float(c))
            else:
                stack.append(op[c](stack.pop(), stack.pop()))
    except ZeroDivisionError:
        return 0

    return stack[0]

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

answer_string = ""
def main():
    global answer_string
    print_rules()
    while True:
        digits = [ ]
        while not digits:
            digits = gen_4_digits()
            (valid, answer_string) = can_make_24(digits)
            if not valid:
                digits = [ ]

        print("\nYour digits:", " ".join([str(d) for d in digits]))
        while True:
            answer = get_valid_answer(digits)
            result = evaluate_answer(answer)
            print("Your total is: {0}".format(int(result)))
            if abs(result - 24) < 0.01:
                print("You got it!")
                print("The expected answer was:", answer_string)
                break
            else:
                print("Try again.")
    
try:
    main()
except KeyboardInterrupt:
    print("\nThe expected answer was:", answer_string)
    print("Thanks for playing!")

