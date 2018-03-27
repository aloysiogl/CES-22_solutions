#!/usr/bin/python3

import turtle


# Question

# Write a program to draw a star shape using a void function


# Function for drawing the star


def drawStar(turtle):
    # Using degrees units

    turtle.degrees()

    '''
    The amount the turtle should spin is:

    180 - 360    1  = 144
          --- * ---
           5     2
    '''

    # Setting up orientation

    turtle.left(36)

    # Drawing the polygon

    for i in range(0, 5):
        turtle.forward(100)
        turtle.left(144)

    # End animation

    turtle.left(360)

    # Hiding turtle

    turtle.hideturtle()


# Getting screen


wn = turtle.Screen()

# Setting screen parameters

wn.title("Tartaruga do Aloysio - estrela")

# Creating turtle

aloysio = turtle.Turtle()

# Going to the right place

aloysio.penup()
aloysio.setx(-40)
aloysio.sety(-25)
aloysio.pendown()

# Setting turtle parameters

aloysio.speed(1)
aloysio.pensize(3)
aloysio.color("blue")
aloysio.pencolor("black")
aloysio.shape("turtle")

# Running the draw function

drawStar(aloysio)

# Keeping the window open

wn.mainloop()


