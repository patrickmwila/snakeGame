from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# == screen setup == #
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # turn off animations by default

# create a Snake instance
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# start listening to key events
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    # update screen animations
    screen.update()
    time.sleep(.05)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with food
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 5:
            is_game_on = False
            scoreboard.game_over()

# == exit screen on click == #
screen.exitonclick()
