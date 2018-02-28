#!/usr/bin/python3

import turtle


# Question

# Write a program to draw a pentagon with stars on its vertices


# Function for drawing the star


def drawStar(turtle):
    # Using degrees units

    '''
    The amount the turtle should spin is:

    180 - 360    1  = 144
          --- * ---
           5     2
    '''

    # Setting pen state

    turtle.pendown()

    # Drawing the polygon

    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(144)

    # Putting the pen up

    turtle.penup()


# Getting screen


wn = turtle.Screen()

# Setting screen parameters

wn.title("Tartaruga do Aloysio - estrela pentagono")
wn.bgcolor("lightgreen")

# Creating turtle

aloysio = turtle.Turtle()

# Setting turtle parameters

aloysio.speed(6)
aloysio.pensize(3)
aloysio.color("pink")

# Drawing the shape

side = 350
aloysio.degrees()

# Going to the right place

aloysio.penup()
aloysio.setx(-180)
aloysio.sety(50)

# Loop for drawing polygon

for i in range(1, 6):
    drawStar(aloysio)
    aloysio.forward(side)
    aloysio.right(144)

# Keeping the window open

wn.mainloop()
