from turtle import Turtle, Screen
from screen import Screen as ScreenFunc
from racket import Racket
from score import Score
from ball import Ball
import time

game_is_on = True

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

racket = Racket()
screen_function = ScreenFunc()
score = Score()
ball = Ball()

screen.onkeypress(lambda: racket.move_up(), "Up")
screen.onkeypress(lambda: racket.move_down(), "Down")

direction_up = True

while game_is_on:
    player_racket = racket.rackets[0]
    bot_racket = racket.rackets[1]
    screen.update()
    time.sleep(0.01)
    ball.move_ball()
    score.draw_score()

    if direction_up:
        if racket.rackets[1].ycor() < 200:
            racket.bot_move_up()
        else:
            direction_up = False
    else:
        if racket.rackets[1].ycor() > -200:
            racket.bot_move_down()
        else:
            direction_up = True

    # COllision avec les murs haut & bas
    if ball.ball_list[0].ycor() > 240 or ball.ball_list[0].ycor() < -240:
        ball.change_direction_y()

    # Collision de la balle avec les raquettes
    if (ball.ball_list[0].distance(player_racket) < 75 and ball.ball_list[0].xcor() < -330) or \
       (ball.ball_list[0].distance(bot_racket) < 75 and ball.ball_list[0].xcor() > 330):
        ball.change_direction_x()

    # Collisions de la balle avec un des deux camps
    if ball.ball_list[0].xcor() > 380:
        score.increment_player_score()
        ball.reset_position()
        score.draw_score()


    if ball.ball_list[0].xcor() < -380:
        score.increment_bot_score()
        ball.reset_position()
        score.draw_score()

screen.exitonclick()