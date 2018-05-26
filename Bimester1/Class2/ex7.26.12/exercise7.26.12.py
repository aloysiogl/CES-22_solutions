#!/usr/bin/python3

import turtle
from math import sqrt


# Getting screen


wn = turtle.Screen()

# Setting screen parameters

wn.title("Tartaruga do Aloysio - casa")
wn.bgcolor("lightgreen")

# Creating turtle

aloysio = turtle.Turtle()

# Setting turtle parameters

aloysio.speed(6)
aloysio.pensize(3)
aloysio.color("blue")
aloysio.degrees()
aloysio.speed(1)

listOfpointsAndDirections = [(90, 100), (30, 100), (120, 100), (120, 100), (-135, 100*sqrt(2)), (-135, 100),
                             (-135, 100*sqrt(2)), (-135, 100)]

for (angle, length) in listOfpointsAndDirections:
    aloysio.left(angle)
    aloysio.forward(length)

# Keeping the window open

wn.mainloop()