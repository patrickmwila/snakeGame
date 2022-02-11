from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")

# read from file
with open("data.txt") as input_file:
    score_txt = int(input_file.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score_txt
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

            with open("data.txt", mode="w") as output_file:
                output_file.write(f"f{self.high_score}")

        self.score = 0
        self.update_scoreboard()
