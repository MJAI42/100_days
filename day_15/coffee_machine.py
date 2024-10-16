from menu import menu, resources

wallet = {"quarters": [0.25, 0], 
          "dimes": [0.1, 0],
          "nikles": [0.05, 0],
          "pennies": [0.01, 0]}

#Print resources
def print_resources ():
    for key in resources:
        print(f"{key}: {resources[key]}")

#Choose a coffee
def which_coffee(): 
    switch = True
    while switch:
        coffee = input("What would you like? (espresso / latte / cappuccino): ")
        coffee = coffee.lower()
        if coffee == "espresso" or coffee == "latte" or\
            coffee == "cappuccino":
            cost = menu[coffee]["cost"]
            print(f"The {coffee} costs ${cost}")
            switch = False
            return coffee
        elif coffee == "off" or coffee == "report":
            switch = False
            return coffee
        else:
            print("I didn't understand please try again.")
            switch = True

#Pay for the coffee and return change
def payment(coffee):
    dollar_paid = 0
    print("Please insert coins.")
    for key in wallet:
        wallet[key][1] = int(input(f"How many {key}?: "))
    for key in wallet:
        dollar_paid += wallet[key][0]*wallet[key][1]
    if dollar_paid < menu[coffee]["cost"]:
        for key in wallet:
            wallet[key][1] = 0
        print(f"You inputed ${round(dollar_paid,2)}")
        print(f"Sorry that's not enought money. ${round(dollar_paid,2)} dollars refunded.")
        dollar_paid = 0
        return False
    elif dollar_paid > menu[coffee]["cost"]:
        dollar_paid -= menu[coffee]["cost"]
        print(f"You inputed {round(dollar_paid,2)}")
        print(f"Here is ${round(dollar_paid,2)} dollars in change.")
        return True
    else:
        dollar_paid -= wallet[key][1]
        print(f"You inputed {round(dollar_paid,2)}")
        print("Thank you for giving the exact change.")
        return True

#Make the coffee
def make_coffee(coffee):
    count = 0
    for key in resources:
        if resources[key] < menu[coffee]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            count +=1
    if count == 0:
        print_resources()
        switch_2 = payment(coffee)
        if switch_2:
            for key in resources:
                resources[key] -= menu[coffee]["ingredients"][key]
        print_resources()
    else:
        return 0


def coffee_machine():
    switch = True
    while switch:
        coffee = which_coffee()
        if coffee == "off":
            switch = False
            return 0
        elif coffee == "report":
            print_resources()
        else:
            make_coffee(coffee)

coffee_machine()