from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.add_car()

    def add_car(self):
        for i in range(7):
            self.refresh_car()

    def refresh_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.penup()
        x = random.randint(280, 600)
        y = random.randint(-250, 250)
        new_car.goto(x, y)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)
        if car.xcor() < 200:
            for i in range(7):
                self.refresh_car()

    def move_speed(self):
        self.car_speed += MOVE_INCREMENT





