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
        screen_drawer.penup()
        screen_drawer.color("white")

        # Délimite la table
        screen_drawer.goto(-400, -250)  # Coin inférieur gauche
        screen_drawer.pendown()
        for _ in range(2):
            screen_drawer.forward(800)  # Hauteur de l'écran
            screen_drawer.left(90)
            screen_drawer.forward(500)  # Largeur de l'écran
            screen_drawer.left(90)
        screen_drawer.penup()

        # desinne la ligne médiane
        screen_drawer.goto(self.line_start)
        screen_drawer.left(90)
        for line in range(7):
            screen_drawer.pendown()
            screen_drawer.forward(30)
            screen_drawer.penup()
            screen_drawer.forward(30)

        screen_drawer.goto(self.score_start)
        screen_drawer.write("SCORE", align="center", font=("Arial", 20, "normal"))