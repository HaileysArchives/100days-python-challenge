# More Turtles? 

# class turtle:
#     timmy = Turtle() # Object = Class
#     tommy = Turtle() # timmy, tommy, jenny => instance

# timmy.color = green # State
# tommy.color = purple 

# 동일한 개체의 별도 버전을 가질 수 있다. 

# Build a Turtle Race

# Who will win the race? Enter a color:

from turtle import Turtle, Screen


screen = Screen()
screen.setup(width = 500, height = 400) # 창의 너비와 높이를 설정
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ") # turtle.textinput(title, prompt)
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# tim = Turtle(shape = "turtle")
# tim.penup()
# # tim.shape("turtle")
# tim.goto(x = -230, y = -100) # x값과 y값 정의 


def make_turtles():
    i = 30
    for tcolor in colors:
        t = Turtle()
        t.shape("turtle")
        t.color(tcolor)
        t.penup()
        t.goto(x = -230, y = -70 + i)
        i += 30

make_turtles()

y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(6): # doesn't include 6
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -230, y = y_position[turtle_index])
   

# Initialiser
class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)

screen.exitonclick()


