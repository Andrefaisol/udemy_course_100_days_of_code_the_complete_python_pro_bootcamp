from turtle import Turtle
import pandas


class Quiz(Turtle):
    def __init__(self):
        super().__init__()
        self.correct = 0
        self.hideturtle()
        self.penup()
        self.data = pandas.read_csv("50_states.csv")
        self.state = self.data["state"]
        self.list_state = []
        self.append_state()

    def append_state(self):
        for i in self.state:
            self.list_state.append(i)

    def search_state(self, name):
        info = self.data[self.state == name]
        info_state = info["state"]
        return info_state

    def search_x(self, name):
        info = self.data[self.state == name]
        info_x = info.x
        return info_x

    def search_y(self, name):
        info = self.data[self.state == name]
        info_y = info.y
        return info_y

    def write_state(self, name):
        self.correct += 1
        newx = self.search_x(name)
        newy = self.search_y(name)
        self.goto(x=int(newx), y=int(newy))
        self.write(f"{name}", move=False, font=("Arial", 10, "normal"))

