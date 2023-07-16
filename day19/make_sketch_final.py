from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # tim.left(10)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # tim.right(10)


def clear():
    tim.clear() # clear() is Delete the turtle's drawings from the screen.
    tim.penup()
    tim.home() # home() is Move turtle to the origin.
    tim.pendown()


screen = Screen()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

# onkey()는 인수가 없는 함수만 받을 수 있다. 
# so, onkey(fun, key) => 'fun' is a function with no arguments or None

