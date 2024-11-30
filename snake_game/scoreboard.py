from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.board()

    def board(self):
        self.write(f"Score: {self.score}", align ="center", font=("Arial", 24, "bold"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.board()
    
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over!", align ="center", font=("Arial", 24, "bold"))