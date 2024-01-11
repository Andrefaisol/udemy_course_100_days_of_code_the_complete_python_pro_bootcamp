from turtle import Turtle
YPOS = [0, -20, -40]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.adding()
        self.head = self.snake[0]

    def adding(self):
        for i in range(0, len(YPOS)):
            dubi = Turtle(shape="square")
            dubi.color("green")
            dubi.penup()
            dubi.shapesize(1, 1)
            dubi.setpos(YPOS[i], 0)
            self.snake.append(dubi)

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            xpos = self.snake[x - 1].xcor()
            ypos = self.snake[x - 1].ycor()
            self.snake[x].goto(xpos, ypos)
        self.head.forward(DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
