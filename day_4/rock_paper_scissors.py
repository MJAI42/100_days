import random

#random_int = random.randint(1, 10)
#print(random_int)

#random_num = random.random()
#print(random_num)

#random_float = random.uniform(1, 10)
#print(random_float)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

outcome = ["rock", "paper", "scissors"]

user_choice = input ('Choose between \"rock\" \"paper\" & \"scissors\"').lower()

random_int = random.randint(0, 2)

if (user_choice == outcome[0]):
    if (outcome[random_int] == outcome[0]):
        print("You chose:")
        print (rock)
        print("\nComputer chose:")
        print (rock)
        print("\nYou Draw")
    elif (outcome[random_int] == outcome[1]):
        print("You chose:")
        print (rock)
        print("\nComputer chose:")
        print (paper)
        print("\nYou Loose")
    else:
        print("You chose:")
        print (rock)
        print("\nComputer chose:")
        print (scissors)
        print("\nYou Win")
elif (user_choice == outcome[1]):
    if (outcome[random_int] == outcome[0]):
        print("You chose:")
        print (paper)
        print("\nComputer chose:")
        print (rock)
        print("\nYou win")
    elif (outcome[random_int] == outcome[1]):
        print("You chose:")
        print (paper)
        print("\nComputer chose:")
        print (paper)
        print("\nYou Draw")
    else:
        print("You chose:")
        print (paper)
        print("\nComputer chose:")
        print (scissors)
        print("\nYou Lose")
else:
    if (outcome[random_int] == outcome[0]):
        print("You chose:")
        print (scissors)
        print("\nComputer chose:")
        print (rock)
        print("\nYou Lose")
    elif (outcome[random_int] == outcome[1]):
        print("You chose:")
        print (scissors)
        print("\nComputer chose:")
        print (paper)
        print("\nYou Win")
    else:
        print("You chose:")
        print (scissors)
        print("\nComputer chose:")
        print (scissors)
        print("\nYou Draw")

