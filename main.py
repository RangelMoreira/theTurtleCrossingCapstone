import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

speed = 0.1

player = Player()
screen.listen()
if game_is_on:
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.move_back, 'Down')
cars = []
indexToGenerateCar = 0

scoreBoard = Scoreboard()

while game_is_on:
    indexToGenerateCar += 1
    if indexToGenerateCar % 6 == 0:
        random_integer = random.randint(-240, 230)
        cars.append(CarManager(random_integer))

    for car in cars:
        # Detect collision
        if player.distance(car) <= 20:
            game_is_on = False
            scoreBoard.create_game_over()
        car.move()

    if player.ycor() >= 280:
        player.go_to_begin()
        speed /= 2
        scoreBoard.update_scoreboard()

    time.sleep(speed)
    screen.update()

screen.exitonclick()
