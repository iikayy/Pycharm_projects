from turtle import Turtle, Screen
import random


my_screen = Screen()
my_screen.setup(600, 500)
color = ["red", "blue", "orange", "green", "yellow", "violet"]
choice = my_screen.textinput("Turtle race", f"Welcome to the Turtle race!!! Choose a color {color}: ")
y_cor = [-230, -150, -70,  10, 90, 170]

all_turtle = []

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-280, y_cor[i])
    all_turtle.append(new_turtle)

racing = True
while racing:
    for turtle in all_turtle:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 280:
            racing = False
            winning_turtle = turtle.pencolor()
            if choice == winning_turtle:
                print(f"You've won. The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost. The {winning_turtle} turtle is the winner")


my_screen.exitonclick()