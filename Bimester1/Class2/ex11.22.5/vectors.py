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


def add_vectors(u, v):
    """This function adds vectors"""
    sum = [0]*len(u)

    for i in range(0, len(u)):
        sum[i] = u[i] + v[i]

    return sum


# Tests


test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
