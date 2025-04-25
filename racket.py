from turtle import Turtle

class Racket:
    def __init__(self):
        self.racket_color = "white"
        self.player_init_position = (-350,0)
        self.bot_init_position = (350,0)
        self.rackets = []
        self.create_player_racket()
        self.create_bot_racket()

    def create_bot_racket(self):
        bot = Turtle("square")
        bot.color(self.racket_color)
        bot.shapesize(stretch_wid=5, stretch_len=1)
        bot.penup()
        bot.goto(self.bot_init_position)
        self.rackets.append(bot)

    def bot_move_up(self):
        self.rackets[1].setheading(90)
        self.rackets[1].shapesize(stretch_wid=1, stretch_len=5)
        self.rackets[1].forward(5)

    def bot_move_down(self):
        self.rackets[1].setheading(270)
        self.rackets[1].shapesize(stretch_wid=1, stretch_len=5)
        self.rackets[1].forward(5)

    def create_player_racket(self):
        racket = Turtle("square")
        racket.color(self.racket_color)
        racket.shapesize(stretch_wid=5, stretch_len=1)
        racket.penup()
        racket.goto(self.player_init_position)
        self.rackets.append(racket)

    def move_up(self):
        if self.rackets[0].ycor() < 200:
            self.rackets[0].setheading(90)
            self.rackets[0].shapesize(stretch_wid=1, stretch_len=5)
            self.rackets[0].forward(10)

    def move_down(self):
        if self.rackets[0].ycor() > -200:
            self.rackets[0].setheading(270)
            self.rackets[0].shapesize(stretch_wid=1, stretch_len=5)
            self.rackets[0].forward(10)