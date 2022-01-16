from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    snake.move()
    # when snake and food collide
    if snake.head.distance(food) < 15:
        scoreboard.track_score()
        food.refresh()
        snake.extend()

    # collide with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            # trigger game_over
            game_is_on = False
            scoreboard.game_over()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()