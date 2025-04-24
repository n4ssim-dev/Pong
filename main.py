from turtle import Turtle, Screen
from racket import Racket
import time

game_is_on = True

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()

racket = Racket()

screen.onkeypress(lambda: racket.move_up(), "Up")
screen.onkeypress(lambda: racket.move_down(), "Down")

direction_up = True  # Initialize direction_up outside the loop

while game_is_on:
    screen.update()
    time.sleep(0.01)

    if direction_up:
        if racket.rackets[1].ycor() < 430:
            racket.bot_move_up()
        else:
            direction_up = False  # Change direction when the top boundary is reached
    else:
        if racket.rackets[1].ycor() > -430:
            racket.bot_move_down()
        else:
            direction_up = True  # Change direction when the bottom boundary is reached

screen.exitonclick()
