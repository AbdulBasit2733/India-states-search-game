import pandas
import turtle

screen = turtle.Screen()

screen.colormode(255)

screen.title("India States Game")

img = "419.gif"

screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("states.txt")

all_states = data.state.to_list()

guessed_states = []

while len(all_states) <= 35:

    user_state = screen.textinput(title="Guess the state", prompt="What's Another State?").capitalize()

    if user_state == "Exit":

        missed_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missed_states)

        new_data.to_csv("states_to_learn.csv")

        break

    if user_state in all_states:

        guessed_states.append(user_state)

        t = turtle.Turtle()

        t.penup()

        t.hideturtle()

        states_data = data[data.state == user_state]

        t.goto(float(states_data.x), float(states_data.y))

        t.write(user_state, font=("Times new roman", 7, "bold"))
