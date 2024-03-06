from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.detect_food()

    def detect_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
