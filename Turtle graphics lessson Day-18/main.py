import turtle
from turtle import Turtle, Screen
import random

turtle_timmy = Turtle()

turtle.colormode(255)

turtle_timmy.pensize(1)
turtle_timmy.speed("fastest")

########################################### RETURNS A RANDOM COLOR  ################################

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

####################################    RANDOM MOVEMENT  #################################


# directions = [0, 90, 180, 270]
# for i in range(200):
#     turtle_timmy.forward(20)
#     turtle_timmy.setheading(random.choice(directions))
#     turtle_timmy.backward(30)
#     turtle_timmy.color(random_color())

########################### DRAWING OF SHAPES (TRIANGLE - DECAGON)################
# num_of_sides = [3, 4, 5, 6, 7, 8, 9, 10]
# for num in num_of_sides:
#     for i in range(num):
#         angle = 360 / num
#         turtle_timmy.forward(100)
#         turtle_timmy.right(angle)
#     turtle_timmy.color(random_color())

################## DOES THE SAME THING AS THE CODE ABOVE #####################

# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         turtle_timmy.forward(100)
#         turtle_timmy.right(angle)
#     turtle_timmy.color(color())
#
#
# for i in range(3, 11):
#     draw_shape(i)



###################################### DRAWING A SPIROGRAPH ##################################

# for num in range(0, 360):
#     if num % 10 == 0:
#         turtle_timmy.setheading(num)
#         turtle_timmy.circle(100, 360)
#         turtle_timmy.color(random_color())


################## DOES THE SAME THING AS THE CODE ABOVE #####################
# def draw_spirograph(size_of_gap):
#     for i in range (int(360/size_of_gap)):
#         turtle_timmy.color(random_color())
#         turtle_timmy.circle(100)
#         turtle_timmy.setheading(turtle_timmy.heading() + size_of_gap)
#
# draw_spirograph(5)


screen = Screen()
screen.exitonclick()
