from turtle import Turtle, Screen
t = Turtle()
s = Screen()

def move_forward():
    t.forward(30)
def move_backward():
    t.backward(50)
def turn_left():
    t.left(10)
    
def turn_right():
    t.right(20)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="w",fun=move_forward)
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear_screen, "c")

s.exitonclick()