from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-275, 265)
        self.score = 0
        self.write(f"Score: {self.score}", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 265)
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT)

    def create_game_over(self):
        self.goto(-10, 0)
        self.write(f"Game Over", font=FONT)
