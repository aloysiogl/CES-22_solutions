#!/usr/bin/python3


def round_area(func):
    """
    This decorators rounds the area
    :param func: area function
    :return: the rounded area function
    """

    def round_area_to_return(side):
        """
        This function calculates the rounded area to 2 decimal digits
        :param side: the side of the square
        :return: the area
        """
        return round(func(side), 2)

    return round_area_to_return


@round_area
def get_square_area_with_decorator(side):
    """
    This function calculates the area of a square using the round decorator
    :param side: the side of the square
    :return: the area
    """

    return side*side


def get_square_area_without_decorator(side):
    """
    This function calculates the area of a square
    :param side: the side of the square
    :return: the area
    """

    return side*side


print("Result with decorator", get_square_area_with_decorator(5.1234))
print("Result without decorator", get_square_area_without_decorator(5.1234))
