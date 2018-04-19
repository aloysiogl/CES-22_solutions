#!/usr/bin/python3

from threading import Thread
import multiprocessing
import time


def worker(num):
    """This worker  ultiplies a nuber using a"""
    paralel_square = num*num
    print ('The square of ', num, ' is ', paralel_square)
    return


jobs = []

start = time.clock()

for i in range(5):
    p = multiprocessing.Process(target=worker_1, args=(i, ))
    jobs.append(p)
    p.start()
    p.join()


print('Time for parallel square range 0-4, multiprocessing: ',  str(time.clock() - start))


class Thread1(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        paralel_square = self.num * self.num
        print('The square of ', self.num, ' is ', paralel_square)


start = time.clock()

for i in range(5):
    t = Thread1(i)
    t.start()
    t.join()

print('Time for parallel square range 0-4, threading: ',  str(time.clock() - start))

def worker_2(num):
    """worker function"""
    paralel_sum = 0
    for i in range(10000):
        paralel_sum += num
    print(num, ' times 10000 using additions is ', paralel_sum)
    return


jobs = []

start = time.clock()

for i in range(2):
    p = multiprocessing.Process(target=worker_2, args=(i, ))
    jobs.append(p)
    p.start()
    p.join()


print('Time for parallel square range 0-4, multiprocessing: ',  str(time.clock() - start))


class Thread2(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        paralel_sum = 0
        for i in range(10000):
            paralel_sum += self.num
        print(self.num, ' times 10000 using additions is ', paralel_sum)


start = time.clock()

for i in range(2):
    t = Thread2(i)
    t.start()
    t.join()

print('Time for parallel square range 0-4, threading: ',  str(time.clock() - start))