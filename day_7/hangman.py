import random

#variables
word_list = ["ubuntu", "marvel", "glow", "amazing", "friends", "spidey"]
word_temp_list = []

r_word = random.choice(word_list)
word_temp = ""
char_guess = ""

credit = 6
count = 0
wins = 0

print("Welcome to hangman: Guess the word:")
print(r_word)

#print the dashes
while count < len(r_word):
    word_temp_list.append("-")
    count += 1

for char in word_temp_list:
    word_temp += char

print(word_temp)

while credit > 0 and wins < len(r_word):
    #pick the first character and put it in lower case
    char_guess = input("Please input a character: \n")
    char_guess = char_guess[0].lower()
    count = 0
    while count < len(r_word):
        if r_word[count] == char_guess:
            word_temp_list[count] = char_guess
            count += 1
            wins += 1
            word_temp = ""
            for char in word_temp_list:
                word_temp += char
                print(word_temp)
        else:
            count += 1
    if wins > 0:
        print(f"you win:\n{word_temp}")
    else:
        print("you lose")
        print(word_temp)
        if credit > 0:
            credit -= 1
if credit == 0:
    print("Game Over")