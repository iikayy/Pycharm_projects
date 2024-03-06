from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.l_score = 0
        self.r_score = 0
        self.goto(position)
        self.write(self.score, False, "center", ("italics", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write(self.l_score, False, "center", ("italics", 40, "normal"))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write(self.r_score, False, "center", ("italics", 40, "normal"))