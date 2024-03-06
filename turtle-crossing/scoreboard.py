FONT = ("Courier", 15, "bold")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 250)
        self.write(F"Level: {self.level}", False, "center", FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(F"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)

