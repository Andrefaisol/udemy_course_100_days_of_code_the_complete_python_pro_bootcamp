from turtle import Turtle
from turtle import Screen

maryadi = Turtle()
maryadi.shape('arrow')
maryadi.up()
maryadi.backward(200)
maryadi.down()

# for _ in range(2):
#     for steps in range(20):
#         maryadi.forward(10)
#         maryadi.up()
#         maryadi.forward(10)
#         maryadi.down()
#     maryadi.right(90)
#     for x in range(6):
#         maryadi.forward(10)
#         maryadi.up()
#         maryadi.forward(10)
#         maryadi.down()
#     maryadi.right(90)

degree = {3: 120, 4: 90, 5: 72, 6: 60, 7: 51.4, 8: 45, 9: 40, 10: 36}
listing = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'purple', 'black']
n = 0
for y in degree.keys():
    maryadi.color(listing[n])
    for x in range(y):
        maryadi.forward(100)
        maryadi.right(degree[y])
    n += 1


screen = Screen()
screen.exitonclick()
