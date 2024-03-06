import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.hideturtle()
car_manager.penup()
car_manager.setheading(180)
car_manager.add_car()
screen.listen()
screen.onkey(player.up, "Up")

score_board = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    # Detects when turtle collides with a car
    for cars in car_manager.cars:
        if player.distance(cars) < 20:
            score_board.game_over()
            game_is_on = False

    # Detects when turtle has reached the finish line
    if player.ycor() > 280:
        car_manager.move_speed()
        player.refresh()
        score_board.level_up()

screen.exitonclick()





