from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 275


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            highscore = int(file.read())
        self.highscore = highscore
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(f"Score: {self.score}   High Score: {self.highscore}", move= False, align= "center", font=("Arial", 15, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", move= False, align= "center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 15, "normal"))