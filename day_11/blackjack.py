from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
player = []

def deal_card():
    rand_int = random.randint(0,12)
    return cards[rand_int]

def first_round():
        player.append(deal_card())
        player.append(deal_card())
        dealer.append(deal_card())
        dealer.append(deal_card())

def print_cards():
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {dealer[0]}")

def continue_game(switch, user_input):
     if user_input == "y":
          switch == True
          return switch
     elif user_input == "n":
          switch == False
          return switch

def blackjack_start ():
     user_input = input("Do you want to play a game of Blackjack Type 'y' or 'n': ") 

def dealer_turn ():
     

def fn_blackjack():
    switch = True
    while switch:
        

        print("\n"*100)
        print(logo)
        first_round()
        print_cards()
        switch_2 = True
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        continue_game(switch_2, user_input)
        while sum(player) < 22 and switch_2 == True:
             player.append(deal_card())
             print_cards()
             if sum(player) > 21:
                  break
             user_input = input("Type 'y' to get another card, type 'n' to pass: ")
             continue_game(switch_2, user_input)
        if sum(player) > 21:
             print()
        switch = False

fn_blackjack()
