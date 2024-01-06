from prettytable import PrettyTable
from turtle import Turtle
from turtle import Screen

# slowly = Turtle()
# slowly.shape("turtle")
# slowly.color("green")
# slowly.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Charmander", "Fire"],
        ["Tortoise", "Water"],
        ["Bulbasaur", "Grass"],
    ]
)

table.align["Pokemon"] = "l"
table.align["Type"] = "l"
print(table)
