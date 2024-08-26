import random
import math
heads_tails = input('Do you want \"Heads\" or \"Tails\"?\n').lower()
random_num = random.random() * 100
random_num = round(random_num)

if (random_num % 2 == 0):
    if(heads_tails == "heads"):
        print("You win it is Heads")
    else:
        print("You loose it is Heads")
elif (random_num % 2 != 0):
    if (heads_tails == "tails"):
        print("You win it is Tails")
    else:
        print("You loose it is Tails")