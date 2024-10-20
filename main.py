import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
# car = CarManager(-100)
player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, 'Down')
cars = []

while game_is_on:

    random_integer = random.randint(-270, 270)
    cars.append(CarManager(random_integer))
    print(random_integer)
    time.sleep(0.1)
    screen.update()
    cars[0].move()

screen.exitonclick()
