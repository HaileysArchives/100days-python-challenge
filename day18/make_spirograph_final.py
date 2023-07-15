import random
import turtle as t 

t.colormode(255)
t.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color 

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap) # 방향을 돌림

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()



# tim.speed("fastest")
# tim.circle(100)
# tim.circle(random_color())
# current_heading = tim.heading() # 0.0 위치 
# tim.setheading(current_heading + 10)
# tim.circle(100)


# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading + 10) # 방향을 돌림
