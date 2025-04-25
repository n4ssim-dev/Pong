import turtle
from score import Score

class Screen:
    def __init__(self):
        self.line_start = (0, -250)
        self.score_start = (0, 210)
        self.drawer = None
        self.score = Score()
        self.draw_screen()

    def draw_screen(self):
        screen_drawer = turtle.Turtle()
        screen_drawer.hideturtle()
        screen_drawer.goto(self.line_start)
        screen_drawer.color("white")
        screen_drawer.left(90)

        for line in range(9):
            screen_drawer.pendown()
            screen_drawer.forward(30)
            screen_drawer.penup()
            screen_drawer.forward(30)

        self.drawer = screen_drawer
