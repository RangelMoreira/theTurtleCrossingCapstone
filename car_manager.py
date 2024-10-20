import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, y_position):
        self.y_position = y_position
        super().__init__()
        self.x_position = 250
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(COLORS))
        self.goto(self.x_position, self.y_position)
        self.move_speed = 0.1
        self.left(90)

    def move(self):
        self.x_position -= STARTING_MOVE_DISTANCE
        self.goto(self.x_position, self.y_position)
        
