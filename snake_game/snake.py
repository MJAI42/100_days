from turtle import Turtle, Screen
from scoreboard import Scoreboard

MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SIZE = 0.5
COLOR = "green"

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

#Creates one snake
    def one_snake(self):
            self.snake = Turtle("square")
            self.snake.color(COLOR, COLOR)
            self.snake.shapesize(SIZE,SIZE,1)
            self.snake.penup()

#Creates a snake of 3 squares and places it in the middle of the screen 
    def create_snake(self):
            x = 0
            for i in range (0, 3):
                self.one_snake()
                self.snake.setposition(x,0)
                x -= MOVE_DISTANCE
                self.snake_body.append(self.snake)

#Moves the snake forward   
    def move(self):
        for i in range (len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

#Adds a snake body part when it eats
    def add_snake(self):
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.one_snake()
        self.snake.setposition(x,y)
        self.snake_body.append(self.snake)       

#Checks if the snake hit the wall or body
    def hit_a_wall(self):
        x = self.snake_body[0].xcor()
        y = self.snake_body[0].ycor()
        for i in range(len(self.snake_body) - 1):
            x_snake = self.snake_body[i + 1].xcor()
            y_snake = self.snake_body[i + 1].ycor()
            if x == x_snake and y == y_snake:
                return False
        if x == 290:
            return False
        elif x == -290:
            return False
        elif y == 290:
            return False
        elif y == - 290:
            return False
        else:
            return True

#Rotates the snake up:
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

#Rotates the snake down:
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   

#Rotates the snake left:
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

#Rotates the snake right:
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)