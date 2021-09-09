#####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")



def move_1():
    for _ in range(4):
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(100)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


step = 0


while step != 4:
    move_1()
    step +=1


######## Challenge 1 - Draw a Square ############

