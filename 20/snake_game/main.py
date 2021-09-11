import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()