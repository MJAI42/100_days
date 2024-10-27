import colorgram
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("triangle")
tim.color("royal blue")
tim.speed(20)
tim.pensize(1)
turtle.colormode(255)

#Choosing Random Colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color

#Drawing Different Shapes
def poly_draw():
    i = 3
    for _ in range(20):
        tim.color(random_color())
        for _ in range(i):
            tim.forward(100)
            angle = 360 / i
            tim.right(angle)
        i += 1

#Moving in a random walk
def random_walk(tim):
    direction = [0, 90, 180, 270]
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(40)

#Drawing a spirograph
def draw_spriro():
    angle = 5
    num_circles = int(360/angle)
    for _ in range(num_circles):
        tim.circle(100)
        tim.left(angle)
        tim.color(random_color())

#Drawing Damien Hirst
def extract_color():
    dot_colors = colorgram.extract('polka_dots.jpg', 100)
    dot_list = []
    for color in dot_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        dot_list.append(new_color)
    return dot_list

dot_colors = extract_color()
width = 10
height = 10
dot_size = 20
def draw_damien(dot_colors, width, height, dot_size):
    y = -100
    tim.penup()
    for _ in range(height):
        x = -100
        tim.setpos(x, y)
        for _ in range(width):
            tim.dot(dot_size, random.choice(dot_colors))
            x += 50
            tim.setpos(x, y)
        y += 50
    

draw_damien(dot_colors, width, height, dot_size)
screen = Screen()
screen.exitonclick()