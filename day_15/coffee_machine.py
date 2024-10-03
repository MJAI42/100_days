from menu import menu, resources

wallet = {"quarters": [0.25, 0], 
          "dimes": [0.1, 0],
          "nikles": [0.05, 0],
          "pennies": [0.01, 0]}

def which_coffee():
    switch = True
    while switch:
        coffee = input("What would you like? (espresso / latte / cappuccino): ")
        coffee = coffee.lower()
        if coffee == "espresso" or coffee == "latte" or\
            coffee == "cappuccino" or coffee == "off" or coffee == "report":
            switch = False
            return coffee
        else:
            print("I didn't understand please try again.")
            switch = True

def payment(coffee):
    dollar_paid = 0
    print("Please insert coins.")
    for key in wallet:
        wallet[key][1] = input(f"How many {key}?: ")
    for key in wallet:
        dollar_paid += wallet[key][1]
    if dollar_paid < menu[coffee]["cost"]:
        for key in wallet:
            wallet[key][1] = 0
        print(f"Sorry that's not enought money. ${round(dollar_paid,2)} dollars refunded.")
        dollar_paid = 0
        return False
    elif dollar_paid > wallet[key][1]:
        dollar_paid -= wallet[key][1]
        print(f"Here is ${round(dollar_paid,2)} dollars in change.")
        return True
    else:
        dollar_paid -= wallet[key][1]
        return True




def make_coffee(coffee):
    switch = True
    for key in resources:
        if resources[key] >= menu[coffee][key]:
            switch = True
        else:
            print(f"Sorry there is not enough {key}.")
            switch = False
    if switch == True:
            for key in resources:
                resources[key] -= menu[coffee]["ingredients"][key]


def coffee_machine():
    switch = True
    while switch:
        coffee = which_coffee()
        if coffee == "off":
            switch = False
            return 0
        elif coffee == "report":
            for key in resources:
                print(f"{key}: {resources[key]}")
        else:
            
coffee_machine()