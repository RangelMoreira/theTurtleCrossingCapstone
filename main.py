import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, 'Down')

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()