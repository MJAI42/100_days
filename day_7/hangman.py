import random

from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

word_temp_list = []
r_word = random.choice(hangman_words.word_list)
word_temp = ""
char_guess = ""
credit = 0
count = 0
wins = 0
game_wins = 0

print("Welcome to hangman: Guess the word:")

#print the dashes
while count < len(r_word):
    word_temp_list.append("-")
    count += 1

for char in word_temp_list:
    word_temp += char

print(word_temp)

while credit < 6 and game_wins < len(r_word):
    #pick the first character and put it in lower case
    print(f"****************************{6 - credit}/6 LIVES LEFT****************************")
    char_guess = input("Please input a character: \n")
    char_guess = char_guess[0].lower()

    count = 0
    wins = 0
    if char_guess in word_temp:
        print(f"You already guessed {char_guess}, guess another letter.")
    else:
        #check if the letter is in the word
        while count < len(r_word):
            if r_word[count] == char_guess:
                word_temp_list[count] = char_guess
                count += 1
                wins += 1
                game_wins += 1
                word_temp = ""
                for char in word_temp_list:
                    word_temp += char
            else:
                count += 1
        if wins > 0:
            print(f"you win:\n{word_temp}")
        else:
            print(f"You guessed {char_guess}, that's not in the word. You lose a life.")
            print(word_temp)
            if credit < 6:
                credit += 1
        print(HANGMANPICS[credit])
#end the game
if credit == 6:
    print("***********************YOU LOSE - GAME OVER***********************")
else:
    print("***********************YOU WIN - GAME OVER***********************")


