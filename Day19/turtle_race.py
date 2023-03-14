from turtle import Turtle,Screen
import random

screen = Screen()
#tim = Turtle()

is_race_on = False
screen.setup(width=700,height=500)
user_bet = screen.textinput(title="Make your Input",prompt="Which Turtle will win the race?, Enter a color: ")
print(user_bet)
colors = ["red","orange","green","blue","purple","black","yellow","brown","pink"]
y_positions = [-110,-70,-30,10,50,80,120,160]

all_turtles = []

for turtle_index in range(0,8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-330,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You Lost !! The {winning_color} turtle is the winner!!")
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
        




screen.exitonclick()