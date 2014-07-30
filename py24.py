#!/usr/bin/env python
# "24" Game
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

Press <ctrl>+c to exit. Good Luck!"""

from __future__ import print_function
import py24util
import random
import re
import operator as ops
op = {
    '+' : ops.add,
    '-' : ops.sub,
    '*' : ops.mul,
    '/' : ops.div
}

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

answer_string = ""
def main():
    global answer_string
    print_rules()
    while True:
        digits = [ ]
        while not digits:
            digits = gen_4_digits()
            (valid, answer_string) = py24util.can_make_24(digits)
            if not valid:
                digits = [ ]

        print("\nYour digits:", " ".join([str(d) for d in digits]))
        while True:
            answer = py24util.get_valid_input("Answer: ", sanitize_answer,
                                              digits)
            result = evaluate_answer(answer)
            print("Your total is: {0}".format(int(result)))
            if abs(result - 24) < 0.01:
                print("You got it!")
                print("The answer that verified these numbers was:",
                      answer_string)
                break
            else:
                print("Try again.")
    
try:
    main()
except KeyboardInterrupt:
    print("\nThe answer that verified these numbers was:", answer_string)
    print("Thanks for playing!")

