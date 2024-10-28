from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_fwd():
    tim.forward(10)
def move_bkw():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear_screen():
    tim.reset()
screen.onkey(move_fwd, "w")
screen.onkey(move_bkw, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
