from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey( snake.up, "Up")
screen.onkey( snake.down, "Down")
screen.onkey( snake.left, "Left")
screen.onkey( snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()


    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

   # DETECT COLLISION WITH BODY
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score_board.reset()
            snake.reset()


screen.exitonclick()