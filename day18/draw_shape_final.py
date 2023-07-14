import turtle as t
import random
from turtle import Screen


tim = t.Turtle()
tim.shape("turtle")
tim.width(4)


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

        change_color()


for shape in range(3, 11):
    draw_shape(shape)


screen = Screen()
screen.exitonclick()