from turtle import  Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal"))

    def refresh(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(" GAME OVER", True, align="center", font=("Arial", 24, "normal"))
