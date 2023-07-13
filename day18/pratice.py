# import turtle as tur

# tur.shape("turtle")
# tur.color("green")

# def drawdot(space, x):
#   for i in range(x):
    
#     tur.dot()
#     tur.forward(space)

# tur.penup()
# drawdot(10, 100)

# Draw a Dashed Line

# turtle.pendown() # drawing when moving.
# turtle.penup() # no drawing when moving.

import turtle as t

tim = t.Turtle()
tim.shape("circle")
tim.color("hotpink")
tim.width(5)

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

