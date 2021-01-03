import turtle
import random

start_points = [
    (0, 0),
    (100, 0),
    (50, 86.6)
]

pos = (1, 1)

turtle.penup()
turtle.screensize(120, 120)
turtle.setworldcoordinates(-10, -10, 110, 110)

for point in start_points:
    turtle.goto(point)
    turtle.dot()

for i in range(10000):
    toward = random.choice(start_points)
    pos = (
        (pos[0] + toward[0]) / 2,
        (pos[1] + toward[1]) / 2
    )
    turtle.goto(pos)
    turtle.dot()
turtle.done()
