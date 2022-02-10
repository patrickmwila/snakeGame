from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes text on the screen"""
        self.write(
            f"Score: {self.score}", move=False, align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        """Increases the score when the snake hits the food"""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays GAME OVER"""
        self.goto(0, 0)
        self.write(
            f"GAME OVER", move=False, align=ALIGNMENT,
            font=FONT
        )
