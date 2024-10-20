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

    time.sleep(0.05)
    screen.update()

screen.exitonclick()
