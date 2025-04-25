import turtle
from score import Score

class Screen(Score):
    def __init__(self):
        super().__init__()
        self.line_start = (0,-500)
        self.score_start = (0,450)
        self.score = Score().score
        self.bot_score = Score().bot_score
        self.drawers = []
        self.draw_screen()
        self.draw_score()

    def draw_screen(self):
        screen_drawer = turtle.Turtle()
        screen_drawer.hideturtle()
        screen_drawer.goto(self.line_start)
        screen_drawer.color("white")
        screen_drawer.left(90)

        for line in range(9):
            screen_drawer.pendown()
            screen_drawer.forward(50)
            screen_drawer.penup()
            screen_drawer.forward(50)

        self.drawers.append(screen_drawer)

    def draw_score(self):
        drawer = self.drawers[0]
        drawer.goto(self.score_start)
        drawer.write("SCORE",align="center",font=("Arial",33,"normal"))
        drawer.goto(self.score_start[0],self.score_start[1] -50)
        drawer.write(f"{self.score} | {self.bot_score}", align="center", font=("Arial", 33, "normal"))