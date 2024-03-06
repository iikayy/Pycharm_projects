import random
from turtle import Turtle
from random import Random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
ALIGNMENT = "center"
FONT = ("italics", 12, "normal")

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 5
        self.create_car()

    def create_car(self):
        for i in range(3):
            self.new_car = Turtle()
            self.hideturtle()
            self.new_car.shape("square")
            self.new_car.shapesize(1, 2)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            x = random.randint(380,600)
            y = random.randint(-250, 250)
            self.new_car.goto(x , y)
            self.cars.append(self.new_car)

    def move(self):
        for self.new_car in self.cars:
            self.new_car.backward(self.car_speed)
        if self.new_car.xcor() < 380:
            self.create_car()

    def increase_speed(self):
        self.car_speed *= 1.5

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", False, ALIGNMENT, FONT)
