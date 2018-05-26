#!/usr/bin/python3


from threading import Thread, RLock
import random
import time


# Holds the items
class Box:
    lock = RLock()

    def __init__(self):
        """
        Initializes the list of items in the box
        """
        self.items = []

    def add(self, item):
        """
        :param item: item to be added
        """
        Box.lock.acquire()
        self.items.append(item)
        Box.lock.release()

    def get(self):
        """
        gets the next item in the box
        :return: the item
        """
        Box.lock.acquire()
        if len(self.items) > 0:
            item = self.items.pop(0)
            Box.lock.release()
            return item
        Box.lock.release()


class Producer(Thread):
    def __init__(self, box):
        """
        :param box: the box of items
        """
        Thread.__init__(self)
        self.box = box

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)

            self.box.add(item)

            print('Producer notify: item N%d added to the box by %s' % (item, self.name))

            time.sleep(1)
        Consumer.not_over = False


class Consumer(Thread):
    not_over = True

    def __init__(self, box):
        """
        :param box: the box of items
        """
        Thread.__init__(self)
        self.box = box

    def run(self):
        while Consumer.not_over:
            item = self.box.get()

            if item is not None:
                print('Consumer notify: %d removed from box by %s' % (item, self.name))


box = Box()

t1 = Producer(box)

t2 = Consumer(box)
t3 = Consumer(box)
t4 = Consumer(box)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
