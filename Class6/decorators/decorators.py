#!/usr/bin/python3


def round_area(func):
    def round_area_to_return(side):
        return round(func(side), 2)

    return round_area_to_return


@round_area
def get_square_area_with_decorator(side):
    return side*side


def get_square_area_without_decorator(side):
    return side*side


print("Result with decorator", get_square_area_with_decorator(5.1234))
print("Result without decorator", get_square_area_without_decorator(5.1234))
