import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()

state_list = []
state_num = len(state_list)
while state_num < 50:
    answer = screen.textinput(f"{len(state_list)}/50 States Correct", "What's another state name")
    guess = answer.title()
    state = data[data.state == guess]

    if guess in state_names:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state.x), int(state.y))
        tim.write(guess)
        state_list.append(guess)

    # if guess == "Exit":
    #     states_to_learn = []
    #     for state in state_names:
    #         if state not in state_list:
    #             states_to_learn.append(state)
    #         new_state = pandas.DataFrame(states_to_learn)
    #         new_state.to_csv("states_to_learn.csv")
    #     break

    if guess == "Exit":
        states_to_learn = [state for state in state_names if state not in state_list]
        new_state = pandas.DataFrame(states_to_learn)
        new_state.to_csv("states_to_learn_everyday.csv")
        break

