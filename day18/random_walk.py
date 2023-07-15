# Draw a Random Walk

import turtle 
import random
from turtle import Screen

tim = turtle.Turtle()
tim.speed(5)
tim.width(4)
tim.shape("turtle")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)

directions = [0, 90, 180, 270]

while True:
    tim.forward(50)
    tim.setheading(random.choice(directions))
    change_color()

screen = Screen()
screen.exitonclick()