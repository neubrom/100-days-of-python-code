from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + 0.2
        new_y = self.ycor() + 0.2
        self.goto(new_x, new_y)