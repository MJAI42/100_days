import random
from art import logo, vs
from game_data import data


#chooses a candidate
def shuffle(the_candidate):
    del the_candidate[:]
    int_rand = random.randint(0, len(data))
    for i in range (0, len(data[int_rand])):
        the_candidate.append(data[int_rand][i])

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
#def compare (the_candidates, ab):
     


def the_game():
    the_candidates = {'a':[], 'b':[]}
    print(logo)
    shuffle(the_candidates['a'])
    print(f"Compare A: {the_candidates['a'][0]}, a {the_candidates['a'][2]}, from {the_candidates['a'][3]}")
    print(vs)
    shuffle(the_candidates['b'])
    print(f"Compare B: {the_candidates['b'][0]}, a {the_candidates['b'][2]}, from {the_candidates['b'][3]}")
    ab = a_or_b()

the_game()
