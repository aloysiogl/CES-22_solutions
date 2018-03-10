#!/usr/bin/python3

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left.
    """
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
    We're assuming here that the_board is a permutation of column
    numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def tryBoardSize(size):
    import random
    import time
    rng = random.Random()  # Instantiate a random number generator

    bd = list(range(size))  # Generate initial permutation

    num_found = False
    tries = 0

    currentTime = time.time()

    while not num_found:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries in {2:.3f} seconds.".format(bd, tries, time.time() - currentTime))
            tries = 0
            num_found = True


def main():
    tryBoardSize(4)
    tryBoardSize(12)

    # From running tests size 16 is the maximum to solve under a minute
    tryBoardSize(16)


main()
