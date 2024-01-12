from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
POSITION = [(-350, 0), (350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
user1 = Paddle(POSITION[0])
user2 = Paddle(POSITION[1])
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=user2.moveup)
screen.onkey(key="Down", fun=user2.movedown)
screen.onkey(key="w", fun=user1.moveup)
screen.onkey(key="s", fun=user1.movedown)

speed = 0.1
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(user2) < 49 and ball.xcor() > 335 or ball.distance(user1) < 49 and ball.xcor() < -335:
        ball.bounce_x()
        speed *= 0.75

    if ball.xcor() > 380:
        speed = 0.12
        ball.reset_pos()
        score.p1_goal()
    if ball.xcor() < -380:
        speed = 0.12
        ball.reset_pos()
        score.p2_goal()

screen.exitonclick()
