from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 275


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(f"Score: {self.score}", move= False, align= "center", font=("Arial", 15, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 15, "normal"))