from turtle import Turtle, Screen
from screen import Screen as ScreenFunc
from racket import Racket
from score import Score
import time

game_is_on = True

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()

racket = Racket()
screen_function = ScreenFunc()
score = Score()

screen.onkeypress(lambda: racket.move_up(), "Up")
screen.onkeypress(lambda: racket.move_down(), "Down")

direction_up = True

while game_is_on:
    screen.update()
    time.sleep(0.01)

    if direction_up:
        if racket.rackets[1].ycor() < 400:
            racket.bot_move_up()
        else:
            direction_up = False
    else:
        if racket.rackets[1].ycor() > -400:
            racket.bot_move_down()
        else:
            direction_up = True

screen.exitonclick()
