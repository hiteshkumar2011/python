from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.xmove
        new_ycor = self.ycor() + self.ymove
        self.goto(new_xcor,new_ycor)
    
    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        
