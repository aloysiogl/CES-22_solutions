#!/usr/bin/python3

import turtle
from time import sleep

# Question

# Use for loops to make a turtle draw these regular polygons (regular means all sides the same
# lengths, all angles the same):
# ◦ An equilateral triangle
# ◦ A square
# ◦ A hexagon (six sides)
# ◦ An octagon (eight sides)


# Function for drawing polygons


def drawPoly(nSides, turtle, side = 50):
    # Turtle speed

    turtle.speed(1)

    # Turtle style

    turtle.color("blue")
    turtle.shape("turtle")
    turtle.pencolor("black")
    turtle.pensize(3)

    # Using degrees units

    turtle.degrees()

    # Showing turtle

    turtle.showturtle()

    # Drawing the polygon

    for i in range(0, nSides):
        turtle.forward(side)
        turtle.left(360/nSides)

    # End animation

    turtle.left(360)

    # Hiding turtle

    turtle.hideturtle()

# My turtle example

wn = turtle.Screen()

# Setting screen parameters

wn.bgcolor("lightblue")
wn.title("Tartaruga do Aloysio")

# Creating turtle

aloysio = turtle.Turtle()

# Drawing polygons

# Triangle

drawPoly(3, aloysio, 200)
sleep(3)
wn.reset()

# Square

drawPoly(4, aloysio, 180)
sleep(3)
wn.reset()

# Hexagon

drawPoly(6, aloysio, 100)
sleep(3)
wn.reset()

# Octagon

drawPoly(8, aloysio, 80)
sleep(3)
wn.reset()

# Keeping the window open

wn.mainloop()


