from turtle import Turtle,Screen

tim = Turtle()


screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(2)

def clockwise():
    tim.right(2)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun= move_forward, key="w")
screen.onkey(fun= move_backwards, key="s")
screen.onkey(fun= counter_clockwise, key="a",)
screen.onkey(fun= clockwise, key="d")
screen.onkey(fun= clear, key="c")




screen.exitonclick()