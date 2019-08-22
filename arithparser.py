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
def parse(expression):
    """
    Take an infix expression and parse it into an AST of simple arithmetic
    operations. Support parenthesis.

    Examples
    
    Given "3 + 4" produce the following AST:
       (+)
      /   \
    (3)   (4)

    A = [3, +, 4]
    parse(A, 0, 1, 2)
    def parse(A, left, curr, right):
        ast = node(curr)

        # parse left side
        if (curr - left) == 1:
            ast.left = node(A[left])
        else:
            newcurr = find_hi_op(A, left, curr)
            ast.left = parse(A, left, newcurr, curr)

        # parse right side
        if (right - curr) == 1:
            ast.right = node(A[right])
        else:
            newcurr = find_hi_op(A, curr, right)
            ast.right = parse(A, curr, newcurr, right)

        return ast

    Given "3 + 4 + 5" produce the following AST:
          (+)
         /   \
       (+)    (5)
      /   \
    (3)   (4)
    
    Given "3 * 4 + 5" produce the following AST:
          (+)
         /   \
       (*)    (5)
      /   \
    (3)   (4)
    
    Given "3 + 4 * 5" produce the following AST:
          (+)
         /   \
       (3)    (*)
             /   \
           (4)   (5)
    
    Given "(3 + 4) * 5" produce the following AST:
          (*)
         /   \
       (+)    (5)
      /   \
    (3)   (4)
    """

