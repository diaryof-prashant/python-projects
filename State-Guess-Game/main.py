import turtle
import pandas as pd

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer=turtle.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's the state name ?").title()

    if answer=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("States missed.csv")
        break
    #If answer is one of the states in all states of the 50_states.csv
    if answer in all_states:
        guessed_state.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)
screen.exitonclick()
