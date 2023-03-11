import random
import turtle as t
from turtle import Screen

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim = t.Turtle()
s = Screen()
tim.pensize(10)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_rgb = (r,g,b)
    return random_rgb

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


s.exitonclick()