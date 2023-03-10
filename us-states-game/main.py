import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
counter = 0
guessed_states = []
not_guessed_states = []

while len(guessed_states) < 50:
    if answer_state == "Exit":
        not_guessed_states = [state for state in state_list if state not in guessed_states]
        learn_states = pandas.DataFrame(not_guessed_states)
        learn_states.to_csv("learn_states.csv")
        break
    elif answer_state in guessed_states:
        answer_state = screen.textinput(title="You've already guessed this state", prompt="What's another state's "
                                                                                          "name?").title()
    elif answer_state in state_list:
        guessed_states.append(answer_state)
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        state_row = data[data["state"] == answer_state]
        turt.setpos(int(state_row.x), int(state_row.y))
        turt.write(answer_state, align="center")
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another "
                                                                                                 "state's "
                                                                                                 "name?").title()
    else:
        answer_state = screen.textinput(title="Incorrect State!!!", prompt="What's another state's name?").title()

if len(guessed_states) == 50:
    print("Congratulations!!! You've successfully guessed all the states in United States of America")
else:
    print("Well done... Better luck next time. Make sure to learn the states in the 'learn_states' file")

# states to learn .csv

