from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
cont = True

while cont:
    options = menu.get_items()
    choice = input(f"What would you like ({options}) ").lower()

    if choice == "off":
        cont = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        enough_resource = coffee_maker.is_resource_sufficient(drink)

        if enough_resource and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
