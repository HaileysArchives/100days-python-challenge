# # Make an Etch-a-Sketch

# W = Forwards
# S = Backwards
# A = Counter-Clockwise # 시계 반대 방향
# D = Clockwise # 시계 방향

from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_counter_clockwise():
    tim.circle(-20)

def move_clockwise():
    tim.circle(20)

screen = Screen()

screen.listen() # onkey()와 같이 키를 입력할 때 상호작용하는 명령어 
screen.onkey(key = "W", fun = move_forwards) # 스페이스 바를 누르면 앞으로 20씩 이동 
screen.onkey(key = "S", fun = move_backwards)
screen.onkey(key = "A", fun = move_counter_clockwise)
screen.onkey(key = "D", fun = move_clockwise)


screen.exitonclick()
