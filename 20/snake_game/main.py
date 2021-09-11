import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)
snake = Turtle()

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.4)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].right(20)

screen.exitonclick()