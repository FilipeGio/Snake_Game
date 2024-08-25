from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='w', fun=snake.up_move)
screen.onkey(key='s', fun=snake.down_move)
screen.onkey(key='d', fun=snake.right_move)
screen.onkey(key='a', fun=snake.left_move)

game_on = True

while game_on:
    snake.move()

    screen.update()
    sleep(0.1)

    if snake.head.distance(food.turtle_food) < 15:
        food.refresh()
        snake.extend()
        score.score_count()

    if snake.hit_check():
        score.game_over()
        break

screen.exitonclick()
