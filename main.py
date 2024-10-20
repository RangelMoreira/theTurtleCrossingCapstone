import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

level = 1
speed = 0.1

player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, 'Down')
cars = []
indexToGenerateCar = 0

while game_is_on:
    indexToGenerateCar += 1
    if indexToGenerateCar % 6 == 0:
        random_integer = random.randint(-230, 230)
        cars.append(CarManager(random_integer))

    for car in cars:
        # Detect collision
        if player.distance(car) <= 20:
            print(player.distance(car))
            print("Game Over")
        car.move()

    if player.ycor() >= 280:
        player.go_to_begin()
        level += 1
        speed /= 2

    time.sleep(speed)
    screen.update()

screen.exitonclick()
