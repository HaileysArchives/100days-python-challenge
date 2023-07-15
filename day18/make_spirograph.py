# Make a Spirograph

import random
from turtle import Screen, Turtle

t = Turtle()
t.color("green")
t.speed(10)
t.width(5)
t.shape("turtle")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    t.color(R, G, B)

for _ in range(12):
    t.circle(80)
    t.right(30)
    change_color()

screen = Screen()
screen.exitonclick()