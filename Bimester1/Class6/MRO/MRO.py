#!/usr/bin/python3


class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        """
        Calculates the area of a shape
        """

        raise Exception('Not implemented')

    def get_geometric_type(self):
        """
        :return: the geometric type
        """
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        """
        Plotas a shape
        :param ratio: the scale
        :param topleft: the position
        """
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        """
        Calculates the area af a hexagon
        :return: the area
        """

        return 'Hexagon area'


class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        """
        Calculates the area af a square
        :return: the area
        """

        return 'Square area'


class PlotterBox(Square, Plotter):
    geometric_type = 'Plotter Box'


class ShapeSquareTest(Square, Shape):
    geometric_type = 'Random'


# Class example
print('Example1' + str(Square.__mro__))

# Extensions created

print('Example2' + str(PlotterBox.__mro__))

# Example3 cant be printed:
# class PlotterBox(Plotter, Square):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Plotter, Square

print('Example4' + str(ShapeSquareTest.__mro__))

# Example3 cant be printed:
# class ShapeSquareTest(Shape, Square):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Shape, Square



