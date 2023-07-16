from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle) # we have to multiple turtle instance.


if user_bet:
    is_race_on = True

while is_race_on: 

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                      
        rand_distance = random.randint(0, 10) # include number 10 
        new_turtle.forward(rand_distance)

 

screen.exitonclick()


# timmy = Turtle()
# tommy = Turtle() 

# 별도의 개체 (서로 다른 인스턴스) 독립적으로 행동이 가능하다. 
# => 오늘 거북이 경주를 통해 각 인스턴스가 자신의 역할을 할 수 있음을 보여주었다 
# (독립적으로 작동하고 동작할 수 있는 여러 개체 만들기)