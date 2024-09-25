import random
from art import logo

#Welcome Print will return 'y' if they want to play and 'n' if they do not want to play
def welcome():
    welcome = "Welcome to the Number Guessing Game!"
    lamp = True
    print("\n" * 20)
    print(logo)
    print(welcome)
    while lamp:
        play = input("Would you like to guess what number I am thinking \
of between 1 and 100 type 'y' for yes and 'n' for no:\n")
        if play == "y":
            lamp = False
            return play
        elif play == "n":
            lamp = False
            return play
        else:
             print("I did not understand can you please try again")

#Difficulty level returns 'easy' or 'hard'
def choose_difficulty():
    lamp = True
    while lamp: 
        difficulty = input ("Choose a difficulty. Type 'easy' or 'hard':\n")
        if difficulty == "easy":
            lamp = False
            return difficulty
        elif difficulty == "hard":
            lamp = False
            return difficulty
        else:
            print("I did not understand can you please try again")

#Number guessing will iterate until all attempts are exhausted
def guess_num(count,rand_num):
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > 0 and guess < 101:
            if guess > rand_num:
                print("Too High!\nGuess again.")
                count -= 1
            elif guess < rand_num:
                print("Too Low!\nGuess again.")
                count -= 1
            elif guess == rand_num:
                print(f"You got it! The answer was {guess}")
                count = 0
        else:
            print("Could you please input an integer between 1 and 100")
    print("GAME OVER!")

def play_again():
    lamp = True
    while lamp:
        play = input("Would you like to play again? Type 'y' for yes and 'n' for no:\n")
        if play == "y":
            lamp = True
            return lamp
        elif play == "n":
            lamp = False
            return lamp
        else:
             print("I did not understand can you please try again")
def game():
    lamp = True
    while lamp:
        play = welcome()        
        if play == "n":
            lamp = False
        elif play == "y":
            difficulty = choose_difficulty()
            if difficulty == "easy":
                count = 10
            elif difficulty == "hard":
                count = 5
            rand_num = random.randint(1,100)
            guess_num(count, rand_num)
            lamp = play_again()
game()
        