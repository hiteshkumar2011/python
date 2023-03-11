import turtle as t
from turtle import Screen
import random

tim =t.Turtle()
s = Screen()


def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_rgb = (r,g,b)
    return random_rgb

tim.speed("fastest")
t.colormode(255)

def spiro_graph(size_of_gap): 
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(50)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(50)

spiro_graph(5)






     


s.exitonclick()
