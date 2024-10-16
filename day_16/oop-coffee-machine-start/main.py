from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
switch = True

while switch:
    order = input(f"What would you like?{menu.get_items()}")
    order = order.lower()
    if order == "off":
        switch == False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "latte" or \
    order == "espresso" or \
    order == "cappuccino":
        drink = menu.find_drink(order)
        resources = coffee_maker.is_resource_sufficient(drink)
        if resources:
            sufficient_funds = money_machine.make_payment(drink.cost)
            if sufficient_funds:
                coffee_maker.make_coffee(drink)
    else:
        print("I did not understand your input please try again.")
        
        

