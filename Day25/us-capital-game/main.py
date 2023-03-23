import time
import turtle
from turtle import Screen, Turtle
import pandas

s = Screen()
s.title("U.S Capital States Game")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)
#print(answer_state)

data = pandas.read_csv("50_states.csv")
# Check if the answer states is one of the 50 States
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = s.textinput(title=f"{len(guessed_states)}/50 States Correct  ",
                               prompt="Whats the another state name ?").title()
    if answer_state == "Exit" or answer_state == "Quit":    ## Exit code
        missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        #t.write(answer_state)

# States not guessed for learning purpose, generating new CSV
states_left = pandas.DataFrame(missing_states)
states_left.to_csv("states_left_to_guess.csv")

#learning_csv =




#turtle.mainloop()
# def get_mouse_click_coor(x,y):
#     print [x,y]
#
# turtle.onscreenclick(get_mouse_click_coor)

#s.exitonclick()

