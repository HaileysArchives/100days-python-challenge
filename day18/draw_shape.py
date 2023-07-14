# Draw a triangle, square(90), pentagon(72), hexagon, heptagon, octagon, nonagon, and decagon.

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.width(3)
# color = ["red", "green", "hotpink", "black", "blue", "purple", "gray"]
# random_color = random.choice(color)

# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)

# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# for _ in range(6):
#     angle = 3
#     for _ in range(angle):
#         tim.forward(100)
#         tim.left(360/angle)
#     angle += 1

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        change_color()


# sides = [3, 4, 5, 6, 7, 8]

# for side in sides:
#     draw_shape(side)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()