    # Turtle Car Crossing Game
    #### Video Demo:  <https://youtu.be/xRBp6yAYCm0>
    #### Description: Turtle Car Crossing Game Using Turtle Python Module

    ## Projects files
        1. project.py:
            this file contains the main driver function and 3 other functions for controlling the turtle, creating the turtle and detecting when the turtle has finished crossing the road.
            it also contains some instance initialization of the car.
            ### Functions:
                + detectCarCollision()
                + detect_car_crossing()
                + create_and_move_car()
        2. Player.py:
            this file contains the class defination of the turtle and it methods and properties.
            ### Class
                + Player
            ### Methods
                + go_up() : move the turtle upward
                + go_to_start() : move the turtle to the start of the line
                + is_at_finish_line() : check if the turtle has reached the finished line
        3. scoreboard.py:
            this file handles the score functionality of the game, defines a class and it appropriate methods and properties.
            it also contains the method that terminate the game when it's over.
            ### Class
                + Scoreboard
            ### Methods
                + update_scoreboard() : update the scoreboard
                + increase_level() : increase the game level
                + game_over() :  display game is over
        4. car_manager.py:
            this file contains the class for turtle car creation.
            ### Class
                + CarManager
            ### Methods
                + create_car()
                + move_car()
                + level_up()
        5. requirements.txt:
            this file contains the required module for execution of this project locally.
        6. text_project.py:
            this file contains the test functions 