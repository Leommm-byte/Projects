import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move()

    # Detect collision with wall
    if player.is_at_finish_line():
        scoreboard.next_level()
        player.starting_position()
        car_manager.increase_speed()

    # Detect collision with car
    for i in car_manager.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
