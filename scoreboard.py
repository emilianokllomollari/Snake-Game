from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def updtae_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.updtae_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def invrease_score(self):
        self.score += 1
        self.updtae_scoreboard()