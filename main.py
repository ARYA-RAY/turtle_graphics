from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)  #remove turtle creation animation
screen.title("SNAKE GAME")

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
    screen.update()   #restart the turtle animation
    time.sleep(0.1)    
    snake.move()

    #detecting collisions with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    #detecting collisions with wall

    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        game_is_on = False
        scoreboard.game_over()

    #detecting collisions with tail

    for i in snake.segments:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()
      
screen.exitonclick()