from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generates a random location for the turtle food object"""
        rand_x = randint(-285, 285)
        rand_y = randint(-285, 265)
        self.goto(rand_x, rand_y)
