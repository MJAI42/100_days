import random

#variables
word_list = ["ubuntu", "marvel", "glow", "amazing", "friends", "spidey"]
r_num = random.randint(0, len(word_list) - 1)
word_guess_list = []

r_word = word_list[r_num]
word_guess = ""
char_guess = ""

credit = 6
count = 0

print("Welcome to hangman: Guess the word:")

#print the dashes
for char in r_word:
    word_guess += "-"
print(word_guess)

#pick the first character and put it in lower case
char_guess = input("Please input a character: \n")
char_guess = char_guess[0].lower()

while credit > 0:
    for char in r_word:
        

    while count < len(r_word):
        if char == char_guess:
            word_guess.append(char_guess)
            count += 1
        else:
            word_guess.append("-")
            count += 1
