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


def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])  # Add remaining items from ys
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def presentInBoth(xs, ys):
    """ Returns a list of elements present both in xs and ys """
    result = []
    xi = 0
    yi = 0
    last = None

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] == ys[yi]:
            if last is not xs[xi]:
                result.append(xs[xi])
                last = xs[xi]
            xi += 1
        else:
            yi += 1


def presentOnlyInFirst(xs, ys):
    """ Returns a list of elements present only in xs list """
    result = []
    xi = 0
    yi = 0
    last = None

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result + presentInBoth(xs[xi:], xs[xi:])

        if xs[xi] < ys[yi]:
            if last is not xs[xi]:
                result.append(xs[xi])
                last = xs[xi]
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
        else:
            yi += 1


def presentOnlyInSecond(xs, ys):
    """ Returns a list of elements present only in ys list """

    return presentOnlyInFirst(ys, xs)


def presentInOneListAtLeast(xs, ys):
    """ Returns a list of elements present in at least one of the lists"""

    inFirst = presentOnlyInFirst(xs, ys)

    inSecond = presentOnlyInSecond(xs, ys)

    inBoth = presentInBoth(xs, ys)

    mergedList = merge(inFirst, inSecond)

    return merge(mergedList, inBoth)


def bagdiff(xs, ys):
    """ uns bagdiff in two lists """
    result = xs
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] == ys[yi]:
            result.remove(xs[xi])
            xi += 1
        else:
            yi += 1


# Tests for the implemented functions
test(presentInBoth([1, 2, 3, 4, 5, 5], [1, 4, 5, 5, 5, 5, 6, 7, 8, 9]) == [1, 4, 5])
test(presentOnlyInFirst([1, 2, 3, 4, 5, 5, 7], [1, 4, 5, 5, 5, 5, 6, 7, 8, 9]) == [2, 3])
test(presentOnlyInSecond([1, 2, 3, 4, 5, 5, 7], [1, 4, 5, 5, 5, 5, 6, 7, 8, 9]) == [6, 8, 9])
test(presentInOneListAtLeast([1, 2, 3, 4, 5, 5, 7], [1, 4, 5, 5, 5, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
test(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
