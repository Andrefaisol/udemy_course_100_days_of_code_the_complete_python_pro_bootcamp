from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Greedy Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.loc()
        snake.add_tail()
        score.adding()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
