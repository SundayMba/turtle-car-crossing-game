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
screen.onkey(player.go_up, "Up")

def detectCarCollision() -> bool:
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            return True
    return False

def detect_car_crossing() -> None:
    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

def create_and_move_car() -> None:
    car_manager.create_car()
    car_manager.move_cars()

def main():
    game_over = False
    while not game_over:
        time.sleep(0.1)
        screen.update()

        create_and_move_car()

        detect_car_crossing()

        if detectCarCollision():
            game_over = True



if __name__ == '__main__':
    main()
    screen.exitonclick()