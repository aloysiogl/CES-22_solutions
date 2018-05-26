#!/usr/bin/python3

import turtle

# My turtle example

wn = turtle.Screen()

# Setting screen parameters

wn.bgcolor("lightgreen")
wn.title("Tartaruga do Aloysio")

# Creating turtle

aloysio = turtle.Turtle()

# Turtle speed

aloysio.speed(10)

# Turtle style

aloysio.color("blue")
aloysio.shape("turtle")
aloysio.pencolor("red")

# Going to initial position

aloysio.penup()
aloysio.sety(100)
aloysio.setx(-100)
aloysio.pendown()

# Drawing shape

for i in range(0, 200):
    aloysio.forward(200)
    aloysio.left(233)
    print(i)
    
# Hiding turtle

aloysio.hideturtle()

wn.mainloop()
