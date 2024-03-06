from turtle import Turtle
from snake import Snake

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score:{self.score}", False, "center", ("italics", 12, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", False, "center", ("italics", 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", False, "center", ("italics", 12, "bold"))