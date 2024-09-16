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

def print_final_cards():
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {dealer}, final score: {sum(dealer)}")     

def continue_game(user_input):
     if user_input == "y":
          switch = True
          return switch
     elif user_input == "n":
          switch = False
          return switch

def dealer_turn ():
     while (sum(dealer) < 17):
          dealer.append(deal_card())
     
def fn_blackjack():
    user_input = input("Do you want to play a game of Blackjack Type 'y' or 'n': ")
    switch = continue_game(user_input)
    while switch:
     dealer.clear()
     player.clear()
     print("\n"*100)
     print(logo)
     first_round()
     print_cards()
     user_input = input("Type 'y' to get another card, type 'n' to pass: ")
     switch_2 = continue_game(user_input)
     while (sum(player) < 22 and switch_2):
          player.append(deal_card())
          print_cards()
          if sum(player) > 21:
               break
          user_input = input("Type 'y' to get another card, type 'n' to pass: ")
          switch_2 = continue_game(user_input)
     if sum(player) > 21:
          print_final_cards()
          print("You lose. :*(")
     elif sum(player) < 22:
          dealer_turn()
          if sum(dealer) > 21 or sum(dealer) < sum (player):
               print_final_cards()
               print("You win. :D")
          elif sum(dealer) == sum(player):
               print_final_cards()
               print("You Draw. :|")
          elif sum(dealer) > sum(player):
               print_final_cards()
               print("You lose. :*(")          
     user_input = input("Do you want to play a game of Blackjack Type 'y' or 'n': ")
     switch = continue_game(user_input)

fn_blackjack()