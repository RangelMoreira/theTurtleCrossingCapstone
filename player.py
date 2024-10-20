from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.position_y = -280
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("black")
        self.goto(0, self.position_y)
        self.move_speed = 0.1
        self.left(90)

    def move_forward(self):
        self.position_y += 20
        self.goto(0, self.position_y)

    def move_back(self):
        if self.position_y > -280:
            self.position_y -= 20
            self.goto(0, self.position_y)

    def go_to_begin(self):
        self.position_y = -280
        self.goto(0, self.position_y)
