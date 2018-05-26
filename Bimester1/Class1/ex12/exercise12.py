#!/usr/bin/python3

import turtle


# Question

# Write a program to draw a clock


# Function for drawing the clock


def drawStar(turtle):
    # Using degrees units

    turtle.degrees()

    # Performing initial stamp

    turtle.stamp()
    turtle.penup()

    # Clock draw cycle

    for i in range(0, 12):
        turtle.forward(190)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.forward(15)
        turtle.stamp()
        turtle.back(225)
        turtle.left(30)

    # Hiding turtle

    turtle.hideturtle()


# Getting screen


wn = turtle.Screen()

# Setting screen parameters

wn.title("Tartaruga do Aloysio - relogio")
wn.bgcolor("lightgreen")

# Creating turtle

aloysio = turtle.Turtle()

# Setting turtle parameters

aloysio.speed(10)
aloysio.pensize(2)
aloysio.color("blue")
aloysio.shape("turtle")

# Running the draw function

drawStar(aloysio)

# Keeping the window open

wn.mainloop()


