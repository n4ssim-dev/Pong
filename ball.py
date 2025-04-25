import turtle

class Ball:
    def __init__(self):
        self.ball_size = (1.5,1.5,1)
        self.ball_list = []
        self.create_ball()

    def create_ball(self):
        ball = turtle.Turtle("circle")
        ball.color("orange")
        ball.penup()
        ball.goto(0,0)
        ball.setheading(-210)
        ball.shapesize(self.ball_size[0],self.ball_size[1],self.ball_size[2])
        self.ball_list.append(ball)

    def move_ball(self):
        ball = self.ball_list[0]
        ball.forward(2)

    def change_direction_y(self):
        ball = self.ball_list[0]
        current_heading = ball.heading()
        new_heading = 360 - current_heading
        ball.setheading(new_heading)

    def change_direction_x(self):
        ball = self.ball_list[0]
        current_heading = ball.heading()
        new_heading = 180 - current_heading
        ball.setheading(new_heading)

    def reset_position(self):
        ball = self.ball_list[0]
        ball.goto(0, 0)
        ball.setheading(-210)