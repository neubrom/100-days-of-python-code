from turtle import Turtle
BALL_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)

    def move(self):
        if self.xcor() < 280 or self.xcor() < -280:
            new_x = self.xcor() + BALL_SPEED
            new_y = self.ycor() + BALL_SPEED
            self.goto(new_x, new_y)
        else:
            new_x = self.xcor() + BALL_SPEED
            new_y = self.ycor() - BALL_SPEED
            self.goto(new_x, new_y)