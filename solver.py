#!/usr/bin/env python
# "24" Game Solver
#
# Copyright (c) 2014, Andrew Sauber
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
"""Enter four digits from 1 to 9, optionally seperated by whitespace only.
Example: 9 1 5 8
The answer for the game "24" using these digits will be printed in prefix form.
Press <ctrl>+c to exit."""

from __future__ import print_function
import util


def print_doc():
    print(__doc__)


def sanitize_input(inp):
    # remove all whitespace by taking advantage of split()
    inp = "".join(inp.split())

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
        inp = util.get_valid_input("Input: ", sanitize_input)
        inp = [int(x) for x in list(inp)]
        (valid, answer_string) = util.can_make_24(inp)

        if valid:
            print("One way to make 24 is:", answer_string)
        else:
            print("No way to make 24")


try:
    main()
except KeyboardInterrupt:
    print("\nThanks for using the 24 solver!")
