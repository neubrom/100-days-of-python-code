import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()


screen.exitonclick()
