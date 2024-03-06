from turtle import Turtle
class Ball(Turtle):
     def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.new_x = 10
        self.new_y = 10
        self.ball_speed = 0.1

     def move(self):
         new_x = self.xcor() + self.new_x
         new_y = self.ycor() + self.new_y
         self.goto(new_x, new_y)

     def bounce_y(self):
        self.new_y *= -1

     def bounce_x(self):
        self.new_x *= -1

     def refresh(self):
         self.goto(0,0)
         self.ball_speed = 0.1
         self.new_x *= -1
         self.new_y *= -1
     def move_speeed(self):
         self.ball_speed *= 0.9