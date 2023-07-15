# More Turtle Graphics, Event listeners, State and Multiple Instances (여러 개의 인스턴스)

# listen() / onkey() e.g

from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)


screen = Screen()
screen.listen() # onkey()와 같이 키를 입력할 때 상호작용하는 명령어 
screen.onkey(key = "space", fun = move_forwards) # 스페이스 바를 누르면 앞으로 10씩 이동 
screen.exitonclick() 


# Functions as Inputs

# function_a(function_b) # 괄호없이 함수 이름만 전달 
# ================================================
def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, add)
print(result)

# 고차함수 : 실제로 다른 함수를 사용
