import turtle

import pandas

from quiz import Quiz

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
quiz = Quiz()
answered_states = []
game_on = True
while game_on:
    answer = screen.textinput(title=f"{quiz.correct}/50 states", prompt="What your answer").title()
    if answer == "Exit":
        not_answered = [i for i in quiz.list_state if i not in answered_states]
        new_data = pandas.DataFrame(not_answered)
        new_data.to_csv("states_that_u_forgot.csv")
        break
    if answer in quiz.list_state:
        quiz.write_state(answer)
        answered_states.append(answer)

    if quiz.correct >= 50:
        game_on = False


turtle.exitonclick()
