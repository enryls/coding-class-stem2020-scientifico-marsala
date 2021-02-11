#!/bin/python3

import turtle
import time

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("green")

tartaruga2 = turtle.Turtle()
tartaruga2.shape("turtle")
tartaruga2.color("red")

sfondo = turtle.Screen()
sfondo.bgcolor("grey")

tartaruga.right(90)
tartaruga.forward(100)

tartaruga2.right(90)
tartaruga2.backward(100)

time.sleep(3)

tartaruga.left(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(100)

tartaruga2.right(90)
tartaruga2.forward(100)
tartaruga2.right(90)
tartaruga2.forward(100)