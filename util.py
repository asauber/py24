# "24" Game utilities
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

from itertools import permutations
import operator as ops

op = {"+": ops.add, "-": ops.sub, "*": ops.mul, "/": ops.truediv}

try:
    input = raw_input
except NameError:
    pass


def get_valid_input(prompt, sanitizer, *args):
    inp = ""
    while inp == "":
        inp = input(prompt)
        try:
            inp = sanitizer(inp, *args)
        except ValueError:
            inp = ""

    return inp


def gen_ops_permutations():
    ops_str = "+-*/"
    return [(a + b + c) for a in ops_str for b in ops_str for c in ops_str]


def solve(digits):
    Ns = permutations(digits)
    Ops = gen_ops_permutations()

    for ns in Ns:
        # For this permutation of the numbers, try all prefix expressions of
        # the form op w op x op y z
        for ops in Ops:
            try:
                result = op[ops[0]](float(ns[1]), float(ns[0]))
                result = op[ops[1]](float(ns[2]), result)
                result = op[ops[2]](float(ns[3]), result)
                if abs(result - 24) < 0.01:
                    answer = "{} {} {} {} {} {} {}".format(
                        ops[2], ns[3], ops[1], ns[2], ops[0], ns[1], ns[0]
                    )
                    return (True, answer)
            except ZeroDivisionError:
                continue

        # For this permutation of the numbers, try all prefix expressions of
        # the form op op w x op y z
        for ops in Ops:
            try:
                result1 = op[ops[0]](float(ns[1]), float(ns[0]))
                result2 = op[ops[1]](float(ns[3]), float(ns[2]))
                result = op[ops[2]](result2, result1)
                if abs(result - 24) < 0.01:
                    answer = "{} {} {} {} {} {} {}".format(
                        ops[2], ops[1], ns[3], ns[2], ops[0], ns[1], ns[0]
                    )
                    return (True, answer)
            except ZeroDivisionError:
                continue

    # none of the permutations were equal to 24
    return (False, "")
