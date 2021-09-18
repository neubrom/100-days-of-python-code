from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
