#!/usr/bin/env python3
#
# "24" Game
#
# Copyright (c) 2014, 2019 Andrew Sauber
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
import util
import random
import re
import operator as ops
import readline

op = {"+": ops.add, "-": ops.sub, "*": ops.mul, "/": ops.floordiv}


def print_rules():
    print(__doc__)


def sanitize_answer(answer, digits):
    # remove all whitespace by taking advantage of split()
    answer = "".join(answer.split())

    # answer is invalid if it does not contain exactly 7 chars
    if len(answer) != 7:
        print("Your answer must contain 3 operators and 4 digits")
        raise ValueError

    # all of the chars must be valid for the set of digits and operations
    valid_chars_string = str("".join(str(d) for d in digits)) + "+-*/"
    for c in answer:
        if c not in valid_chars_string:
            print("Your answer contains an invalid number or operator")
            raise ValueError

    # the answer must take one of these prefix forms
    prefix_patterns = [
        re.compile("[+\-*/][+\-*/][+\-*/]\d\d\d\d"),
        re.compile("[+\-*/][+\-*/]\d\d[+\-*/]\d\d"),
        re.compile("[+\-*/][+\-*/]\d[+\-*/]\d\d\d"),
        re.compile("[+\-*/]\d[+\-*/][+\-*/]\d\d\d"),
        re.compile("[+\-*/]\d[+\-*/]\d[+\-*/]\d\d"),
    ]
    if not any([pattern.match(answer) for pattern in prefix_patterns]):
        print("Your answer isn't in prefix notation")
        raise ValueError

    # the answer is valid
    return answer


def evaluate_answer(answer):
    stack = []

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


def gen_puzzle():
    while not digits:
        digits = [random.randint(1, 9) for _ in range(4)]
        valid, answer_string = util.can_make_24(digits)
        if not valid:
            digits = []
    return digits


def game_loop():
    while True:
        puzzle = gen_puzzle()

        print("\nYour digits:", " ".join([str(d) for d in digits]))
        while True:
            answer = util.get_valid_input("Answer: ", sanitize_answer, digits)
            result = evaluate_answer(answer)
            print("Your total is: {0}".format(int(result)))
            if abs(result - 24) < 0.01:
                print("You got it!")
                print("The answer that verified these numbers was:", answer_string)
                break
            else:
                print("Try again.")


def game():
    print_rules()
    game_loop()


def main():
    game()


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("Thanks for playing!")
