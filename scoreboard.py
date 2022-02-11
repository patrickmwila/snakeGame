from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        """Writes text on the screen"""
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", move=False,
            align=ALIGNMENT, font=FONT
        )

    def increase_score(self):
        """Increases the score when the snake hits the food"""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()