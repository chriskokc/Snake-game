from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.SCORE = 0
        self.write_score(self.SCORE)

    def track_score(self):
        self.SCORE += 1
        # clear the writing everytime updating the score
        self.clear()
        self.write_score(self.SCORE)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",  align=ALIGNMENT, font=FRONT)

    def write_score(self, score):
        self.write(arg=f"Score: {score}",  align=ALIGNMENT, font=FRONT)
