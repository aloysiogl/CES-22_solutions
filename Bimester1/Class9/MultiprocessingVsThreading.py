#!/usr/bin/python3

from threading import Thread
import multiprocessing
import time


def worker(num, multiply_by):
    """
    This worker multiplies a number using additions
    :param num: the number
    :param multiply_by: the multiplying factor
    """

    tot = 0

    for j in range(multiply_by):
        tot += num

    print(num, ' times ', multiply_by, 'using additions is ', tot)
    return


class Threading(Thread):
    def __init__(self, num, multiply_by):
        """
        This thread multiplies a number using additions
        :param num: the number
        :param multiply_by: the multiplying factor
        """
        Thread.__init__(self)
        self.num = num
        self.mult = multiply_by

    def run(self):

        tot = 0

        for j in range(self.mult):
            tot += self.num

        print(self.num, ' times ', self.mult, 'using additions is ', tot)
        return


def compare(num, mult):
    """
    Compares threading and multiprocessing for a multiplication using sums example
    :param num: max number to multiply (starting from 0 to num)
    :param mult: the multiplication factor
    :return: a tuple of times (first the multiprocessing time and second the threading time) and last return is a message
    """

    # Multiprocessing test

    start = time.clock()

    jobs = []

    for i in range(num+1):
        p = multiprocessing.Process(target=worker, args=(i, mult, ))
        jobs.append(p)
        p.start()
        p.join()

    time_m = time.clock() - start

    # Threading test

    start = time.clock()

    for i in range(num+1):
        t = Threading(i, mult)
        t.start()
        t.join()

    time_t = time.clock() - start

    # Comparison message

    message = ""

    if time_t > time_m:
        message = " multiprocessing was better."
    else:
        message = " threading was better"

    # Returning the comparison of times

    return time_m, time_t, message


comparison1 = compare(10, 10)
comparison2 = compare(2, 10000)

print("First comparison multiprocessing took ", comparison1[0], ' and threading took ', comparison1[1], comparison1[2])
print("First comparison multiprocessing took ", comparison2[0], ' and threading took ', comparison2[1], comparison2[2])
