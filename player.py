from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -280:
            self.backward(MOVE_DISTANCE)

    def go_to_begin(self):
        self.position_y = -280
        self.goto(0, self.position_y)
