from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
LEFT = 180


class Paddle:

    def __init__(self):
        pass

    def go_up():
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def go_down():
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")