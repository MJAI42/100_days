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


def hit_a_wall(switch, x, y):
    if x == 290:
        switch = False
    elif x == -290:
        switch = False
    elif y == 290:
        switch = False
    elif y == - 290:
        switch = False
    else:
        switch = True
    return switch

def left():
    snake_body[0].left(90)
    snake_body[0].forward(10)

def screen_left(screen, left):
    screen.onkey(left, "a")
    screen.listen()

def right():
    snake_body[0].right(90)
    snake_body[0].forward(10)

def screen_right(screen, right):
    screen.onkey(right, "d")
    screen.listen()

switch = True


while switch:
    screen.update()
    time.sleep(0.5)
    for i in range (len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)
    snake_body[0].forward(10)
    screen_left(screen, left)
    screen_right(screen, right)
    x = snake_body[0].xcor()
    y = snake_body[0].ycor()
    switch = hit_a_wall(switch, x, y)








# def west():
#     switch = True
#     while switch:
#         x = snake.xcor()
#         y = snake.ycor()
#         x += 10
#         x_1 = x
#         screen.update()
#         time.sleep(1)
#         for snake in snake_body:
#             snake.setposition(x_1, y)
#             x_1 -= 10
#         switch = hit_a_wall(switch, x, y)

# screen.onkey(west, "a")
# # screen.onkey(east, "d")

screen.exitonclick()