import turtle
from quiz import Quiz

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
quiz = Quiz()

game_on = True
while game_on:
    answer = screen.textinput(title=f"{quiz.correct}/50 states", prompt="What your answer").title()
    if answer == "Exit":
        break
    if answer in quiz.list_state:
        quiz.write_state(answer)
    if quiz.correct >= 50:
        game_on = False


turtle.exitonclick()
