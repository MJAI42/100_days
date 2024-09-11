print("Welcome to the secret auction program.")

participants = {}
name = ""
bid = int
another_bidder = ""
switch = True
winner = str
while switch == True:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    participants[name] = bid
    another_bidder = input("Are there any other bidders? Type \'yes\' or \'no\'\n")
    if another_bidder == "yes":
        switch = True
        print("\n" * 20)
    elif another_bidder == "no":
        switch = "False"
print("\n" * 20)
winner = next(iter(participants))
for name in participants:
    if participants[name] > participants [winner]:
        winner = name
print(f"The winner is {winner} with a bid of ${participants[winner]}")