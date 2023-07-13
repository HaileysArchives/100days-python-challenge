# Draw a triangle, square(90), pentagon(72), hexagon, heptagon, octagon, nonagon, and decagon.

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.width(3)
color = ["red", "green", "hotpink", "black"]
random_color = random.choice(color)
tim.color(random_color)

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

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

draw_shape(3)

screen = Screen()
screen.exitonclick()