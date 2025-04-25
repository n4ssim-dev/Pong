import turtle
import random

LIGHT_COLORS = [
    "lightblue",
    "lightcyan",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightyellow",
    "lightcoral",
    "lightgoldenrodyellow",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lavender",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "oldlace",
    "palegoldenrod",
    "papayawhip"
]


class Ball:
    def __init__(self):
        self.ball_size = (1.5,1.5,1)
        self.ball_list = []
        self.ball_speed = 2
        self.create_ball()

    def create_ball(self):
        ball = turtle.Turtle("circle")
        ball.color(random.choice(LIGHT_COLORS))
        ball.penup()
        ball.goto(0,0)
        ball.setheading(-210)
        ball.shapesize(self.ball_size[0],self.ball_size[1],self.ball_size[2])
        self.ball_list.append(ball)

    def move_ball(self):
        ball = self.ball_list[0]
        ball.forward(self.ball_speed)

    def change_direction_y(self):
        ball = self.ball_list[0]
        current_heading = ball.heading()
        new_heading = 360 - current_heading
        ball.setheading(new_heading)
        ball.color(random.choice(LIGHT_COLORS))
        self.ball_speed += 0.5

    def change_direction_x(self):
        ball = self.ball_list[0]
        current_heading = ball.heading()
        new_heading = 180 - current_heading
        ball.setheading(new_heading)
        ball.color(random.choice(LIGHT_COLORS))
        self.ball_speed += 0.5

    def reset_position(self):
        ball = self.ball_list[0]
        ball.goto(0, 0)
        ball.setheading(-210)
        self.ball_speed = 2