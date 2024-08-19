print("Are you specced to ride?")
height = int(input("What is your height?\n"))
if (height > 120):
    print("You are specced to ride.")
    age = int(input("What is your age?\n"))
    if (age < 12):
        print("Child ticket, please pay $5")
        bill = 5
    elif (age <= 18):
        print("Youth ticket, please pay $7")
        bill = 7
    else:
        print("Adult tickets, please pay $12")
        bill = 12
    photo = input ("Do you want a photo? y/n\n")
    if (photo == "y"):
        bill += 3
    
    print (f"You final bill is {bill}")

    
else:
    print("You are not specced to ride")
