print("Are you specced to ride?")
height = int(input("What is your height?\n"))
if (height > 120):
    print("You are specced to ride.")
    age = int(input("What is your age?\n"))
    if (age < 12):
        print("Please pay $5")
    elif (age <= 18):
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You are not specced to ride")