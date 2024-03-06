from turtle import Turtle
ALIGNMENT = "center"
FONT = ("italics", 12, "normal")


class Level (Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        with open("data.txt") as data:
            self.Highest_level = int(data.read())
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level :{self.level}          Highest level :{self.Highest_level}", False, ALIGNMENT, FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def reset(self):
        if self.level > self.Highest_level:
            self.Highest_level = self.level
            with open("data.txt", "w") as data:
                data.write(f"{self.Highest_level}")
        self.level = 0
        self.update_level()


