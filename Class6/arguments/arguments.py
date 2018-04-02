#!/usr/bin/python3


def supermarket(*supermarket_options, **shoppingdict):
    """
    Prints a list of supermarkets and the shoppinglist
    :param supermarket_options: the list of supermarkets
    :param shoppingdict: the list of this=ngs to buy
    """

    print("Supermarket options:")

    for market in supermarket_options:
        print(market)

    print("\nShopping list:")

    for item in shoppingdict:
        print(item, ":", shoppingdict[item])


# Example
supermarket("Walmart", "Extra", "Villareal", Ovos=16, Macarrao=10, Pao=20)