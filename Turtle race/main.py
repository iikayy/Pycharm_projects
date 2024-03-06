from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width= 700, height=500)
color = ["red", "blue", "yellow", "green", "black", "orange", "purple"]
y = [-200, -140, -80, -20, 40, 100, 160]
user_bet = screen.textinput("Turtle race", "Which Turtle will win the race? Enter a color: ")
all_turtles = []

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-330, y[i])
    new_turtle.color(color[i])
    all_turtles.append(new_turtle)

race = True
while race:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            race = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward( rand_distance)





screen.exitonclick()