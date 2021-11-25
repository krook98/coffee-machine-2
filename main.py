from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
coffee_money_machine = MoneyMachine()
real_coffee_maker = CoffeeMaker()
menu = Menu()


def turn_off():
    global turn_on
    turn_on = False


while turn_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        turn_off()
        print("Goodbye")
    elif choice == "report":
        real_coffee_maker.report()
        coffee_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_money_machine.make_payment(drink.cost) and \
                real_coffee_maker.is_resource_sufficient(drink):
            real_coffee_maker.make_coffee(drink)
