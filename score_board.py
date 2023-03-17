from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

