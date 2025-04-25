import turtle

class Score:
    def __init__(self):
        self.score = 0
        self.bot_score = 0
        self.drawer = turtle.Turtle()

    def draw_score(self):
        self.drawer.clear()
        self.drawer.hideturtle()
        self.drawer.color("white")
        self.drawer.penup()
        self.drawer.goto(0, 180)
        self.drawer.write(f"{self.score} | {self.bot_score}", align="center", font=("Arial", 20, "normal"))

    def increment_player_score(self):
        self.score += 1
        self.drawer.clear()
        self.draw_score()

    def increment_bot_score(self):
        self.bot_score += 1
        self.drawer.clear()
        self.draw_score()

    def reset_scores(self):
        self.score = 0
        self.bot_score = 0
        self.draw_score()