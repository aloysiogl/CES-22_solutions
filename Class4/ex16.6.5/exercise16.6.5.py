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

        b = ((self.x - point.x) * point.y - (self.y - point.y) * point.x) / (self.x - point.x)

        a = (self.y - point.y) / (self.x - point.x)

        return a, b


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """

        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def get_points(self):
        """ This function returns all the point of a rectangle """

        corner2 = Point(self.corner.x + self.width, self.corner.y)
        corner3 = Point(self.corner.x, self.corner.y + self.height)
        corner4 = Point(self.corner.x + self.width, self.corner.y + self.height)

        return self.corner, corner2, corner3, corner4

    def __is_interior_point(self, point):
        """ This function determines if a point is interior to this rectangle """

        inX = False
        inY = False

        if (point.x >= self.corner.x) and (point.x <= self.corner.x + self.width):
            inX = True

        if (point.y >= self.corner.y) and (point.y <= self.corner.y + self.height):
            inY = True

        return inX and inY

    def is_colliding(self, rectangle):
        """ This functions determines if a rectangle is colliding to other rectangle"""

        for point in rectangle.get_points():
            if self.__is_interior_point(point):
                return True
        return False


rect1 = Rectangle(Point(0, 0), 2, 3)
rect2 = Rectangle(Point(0, 2), 2, 3)

print(rect1.is_colliding(rect2))
print(rect2.is_colliding(rect1))
