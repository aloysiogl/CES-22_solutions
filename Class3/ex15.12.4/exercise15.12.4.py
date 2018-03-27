#!/usr/bin/python3


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def slope_from_origin(self):
        """ Computes the slope of a line connection the origin and the point """

        return self.y / self.x

    def get_line_to(self, point):
        """ Gets a line to a point given """

        b = ((self.x - point.x)*point.y - (self.y - point.y)*point.x)/(self.x - point.x)

        a = (self.y - point.y)/(self.x - point.x)

        return a, b


# testing the get_line_to function

print(Point(4, 11).get_line_to(Point(6, 15)))


