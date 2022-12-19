import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
# score = Scoreboard()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        for state in missed_states:
            not_guess_answer = data[data.state == state]
            pointer.goto(int(not_guess_answer.x), int(not_guess_answer.y))
            pointer.color('red')
            pointer.write(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        answer = data[data.state == answer_state]
        pointer.goto(int(answer.x), int(answer.y))
        pointer.write(answer_state)
        guessed_states.append(answer_state)
