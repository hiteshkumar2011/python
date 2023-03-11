from turtle import Turtle,Screen
pen = Turtle()
s=Screen()

for _ in range(5):
    pen.forward(20)
    pen.up()
    pen.forward(20)
    pen.down()

s.exitonclick()