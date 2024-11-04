from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_body = []
x = 0

for i in range (0, 3):
    snake = Turtle("square")
    snake.color("white", "green")
    snake.shapesize(0.5,0.5,1)
    snake.penup()
    snake.setposition(x,0)
    x -= 10
    snake_body.append(snake)

switch = True
x = 0
while switch:
    x += 10
    y = x
    screen.update()
    time.sleep(1)
    for snake in snake_body:
        snake.setposition(y, 0)
        y -= 10
    if x == 290:
        switch = False
    else:
        swtich = True

screen.exitonclick()