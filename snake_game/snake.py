from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

#Creates a snake of 3 squares and places it in the middle of the screen 
    def create_snake(self):
            x = 0
            for i in range (0, 3):
                snake = Turtle("square")
                snake.color("white", "green")
                snake.shapesize(0.5,0.5,1)
                snake.penup()
                snake.setposition(x,0)
                x -= 10
                self.snake_body.append(snake)

#Moves the snake forward   
    def move(self):
            for i in range (len(self.snake_body) - 1, 0, -1):
                x = self.snake_body[i - 1].xcor()
                y = self.snake_body[i - 1].ycor()
                self.snake_body[i].goto(x, y)
            self.snake_body[0].forward(10)

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

#Moves the snake left or right:
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
    



