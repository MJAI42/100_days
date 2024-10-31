from turtle import Turtle, Screen
import random 


screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo" , "violet"]
coordinate_y = 100
switch = False
all_turtles = []


for i in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230 , y = coordinate_y)
    coordinate_y -= 30
    all_turtles.append(new_turtle)

if user_bet:
    switch = True

while switch:
    for turtle in all_turtles:
        pace = random.randint(0,10)
        turtle.forward(pace)
        x_cord = turtle.xcor()

        if x_cord > 230:
            switch = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")




screen.exitonclick()