import random
from art import logo, vs
from game_data import data


#chooses a candidate
def shuffle(the_candidate):
    del the_candidate[:]
    int_rand = random.randint(0, len(data) - 1)
    for key in data[int_rand]:
        the_candidate.append(data[int_rand][key])

#outputs users choice
def a_or_b():
    switch = True
    while switch:
        ab = input("Who has more followers? Type 'A' or 'B': ")
        ab = ab.lower()
        if ab == "a":
            switch = False
            return "a"
        elif ab == "b":
            switch = False
            return "b"
        else:
            print("I did not understand please try again.")

#compares both candidates who has more follower count
def compare (the_candidates, ab):
    if the_candidates['a'][2] > the_candidates['b'][2]:
        if ab == 'a':
            return 1
        else:
            return 0
    elif the_candidates['a'][2] < the_candidates['b'][2]:
        if ab == 'b':
            return 1
        else:
            return 0
     


def the_game():
    switch = True
    score = 0
    print("\n"*20)
    print(logo)
    while switch:
        the_candidates = {'a':[], 'b':[]}
        shuffle(the_candidates['a'])
        shuffle(the_candidates['b'])
        print(f"Compare A: {the_candidates['a'][0]}, a {the_candidates['a'][2]}, from {the_candidates['a'][3]}")
        print(vs)
        print(f"Compare B: {the_candidates['b'][0]}, a {the_candidates['b'][2]}, from {the_candidates['b'][3]}")
        ab = a_or_b()
        winner = compare(the_candidates, ab)
        print(winner)
        if winner == 1:
            score += 1
            print("\n"*20)
            print(logo)
            print(f"You're right your current score is: {score}")
        else:
            score += 0 
            print("\n"*20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            switch = False
the_game()
