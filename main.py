from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    screen.listen()
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)
    screen.onkey(key="Up", fun=snake.turn_up)
    screen.onkey(key="Down", fun=snake.turn_down)

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.generate_new()
        snake.add_body()
        score_board.update()
    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_is_on = False
        score_board.game_over()
# detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
