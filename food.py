import turtle
from turtle import Turtle
import random as r

turtle.colormode(255)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.9, 0.9)

        self.color(0, 255, 0)
        self.speed("fastest")
        self.goto(r.randint(-280, 280), r.randint(-280, 280))

    def generate_new(self):
        self.color(0, 255, 0)
        super().goto(r.randint(-280, 280), r.randint(-280, 280))
