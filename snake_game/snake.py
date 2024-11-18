from turtle import Turtle, Screen
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

#Creates a snake of 3 squares and places it in the middle of the screen 
    def create_snake(self):
            x = 0
            for i in range (0, 3):
                snake = Turtle("square")
                snake.color("green", "green")
                snake.shapesize(0.5,0.5,1)
                snake.penup()
                snake.setposition(x,0)
                x -= MOVE_DISTANCE
                self.snake_body.append(snake)

#Moves the snake forward   
    def move(self):
            for i in range (len(self.snake_body) - 1, 0, -1):
                x = self.snake_body[i - 1].xcor()
                y = self.snake_body[i - 1].ycor()
                self.snake_body[i].goto(x, y)
            self.head.forward(MOVE_DISTANCE)

#Checks if the snake hit a wall
    def hit_a_wall(self, switch, x, y):
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

