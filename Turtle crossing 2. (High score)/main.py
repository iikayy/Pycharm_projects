import time
from turtle import Turtle, Screen
from Player import Player
from car import Car
from level import Level

screen = Screen()
screen.setup( 800, 600)
screen.tracer(0)

player = Player()
car = Car()
level = Level()



screen.listen()
screen.onkey(player.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.move()

# Detects when player reaches the finish line, to increase the speed of the cars
    if player.ycor() > 280:
        player.refresh()
        level.level_up()
        car.increase_speed()




# Detects collision between the player and a car
    for car.new_car in car.cars:
        if car.new_car.distance(player) < 20:
            car.game_over()
            level.reset()
            game_on = False









screen.exitonclick()
