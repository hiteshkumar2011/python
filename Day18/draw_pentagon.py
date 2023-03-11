from turtle import Turtle,Screen
import random

t=Turtle()
s=Screen()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_sides(num_sides):
    angle= 360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3,11):
    t.color(random.choice(colours))
    draw_sides(shape_side_n)


s.exitonclick()


