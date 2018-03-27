#!/usr/bin/python3

import sys


def test(did_pass):
    """ Print the result of a test. """

    linenum = sys._getframe(1).f_lineno

    # Get the caller's line number.

    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def scalar_mult(s, v):
    """This function adds vectors"""
    mult = [0]*len(v)

    for i in range(0, len(v)):
        sum[i] = s*v[i]

    return sum


# Tests


test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
