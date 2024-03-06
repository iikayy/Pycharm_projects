# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('damien-hirst.jpeg.webp', 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import turtle
import random
from turtle import Turtle, Screen


color_list = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (200, 142, 33), (116, 155, 171), (124, 79, 98),
              (122, 175, 157), (229, 197, 128),  (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125),
              (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26),
              (38, 32, 34),(80, 148, 170), (162, 26, 21), (236, 165, 170), (98, 125, 160), (167, 207, 192),
              (22, 79, 91), (162, 203, 212)]

tim = Turtle()
turtle.colormode(255)

tim.hideturtle()
tim.penup()
tim.setheading(232)
tim.forward(250)
tim.setheading(0)
def moving_dot():
    for i in range(10):
        tim.forward(50)
        tim.dot(20,random.choice(color_list))

def next_line():
    y = [-150, -100, -50, 0, 50, 100, 150, 200, 250]
    for num in y:
        tim.goto(-154, num)
        moving_dot()

moving_dot()
next_line()

my_screen = Screen()
my_screen.exitonclick()
