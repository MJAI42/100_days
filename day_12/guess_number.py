from art import logo

welcome = "Welcome to the Number Guessing Game!"
switch = True

#Welcome Print
def welcome ():
    print(logo)
    print(welcome)

def choose_difficulty ():
    lamp = True
    while lamp: 
        difficulty = input ("Choose a difficulty. Type 'easy' or 'hard'")
        if difficulty == "easy":
            lamp = False
            return difficulty
        elif difficulty == "hard":
            lamp = False
            return difficulty
        else:
            print("I did not understand can you please try again")

choose_difficulty()

# while switch:
#     play = input("""Would you like to guess what number I am thinking of between 1 and 100 
#                  type 'y' for yes and 'n' for no """)
#     if play == "n":
#         switch = False
#     else: