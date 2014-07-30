# "24" Game utilities
# Copyright (C) Andrew Sauber 2014, All rights reserved

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

def can_make_24(digits):
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
                    answer_string = "{} {} {} {} {} {} {}".format(
                                        ops[2], ns[3],
                                        ops[1], ns[2],
                                        ops[0], ns[1], ns[0])
                    return (True, answer_string)
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
                    answer_string = "{} {} {} {} {} {} {}".format(
                                        ops[2],
                                        ops[1], ns[3], ns[2],
                                        ops[0], ns[1], ns[0])
                    return (True, answer_string)
            except ZeroDivisionError:
                continue

    # none of the permutations were equal to 24
    return (False, "")

