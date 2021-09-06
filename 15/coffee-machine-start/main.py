MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

drink = ""
machine_state = True

# print(resources_now)
# Ask wat would the customer like
"""Prompt user by asking “​ What would you like? (espresso/latte/cappuccino):​”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer."""


def order():
    drink_order = input("​ What would you like? (espresso/latte/cappuccino):​")
    if drink_order not in ("espresso", "latte", "cappuccino", "off", "report"):
        print("Wrong input, order again!")
        order()
    return drink_order


# Turn off the Machine
"""Turn off the Coffee Machine by entering “​ off​” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens."""


def machine_on_off(drink_order):
    """check if order is OFF, input - drink order """
    if drink_order in ("espresso", "latte", "cappuccino", "report"):
        return True
    elif drink_order == "off":
        return False


# Print report.
"""When the user enters “report” to the prompt,
a report should be generated that shows the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5"""


def report(drink_order, resources_c):
    if drink_order == "report":
        for key, value in resources_c.items():
            print(key, ':', value, end=" ")
            if key in ("water", "milk"):
                print("ml")
            elif key in ("coffee"):
                print("g")
            else:
                print("$")


# Check resources sufficient?
"""a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “​ Sorry there is not enough water.​
”
c. The same should happen if another resource is depleted, e.g. milk or coffee."""


def check_resources(drink_order, resources_check, menu_check):
    """compare needed resources for drink order according to MENU"""
    if drink_order != "report":
        for keys_l in list(menu_check[drink_order]['ingredients'].keys()):
            if resources_check.get(keys_l) - MENU[drink]['ingredients'].get(keys_l) >= 0:
                return True
            else:
                print(f"Sorry there is not enough {keys_l}.")
                return False


# Process coins.
""" a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""

#  Check transaction successful?
"""a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “​ Sorry that's not enough money. Money refunded.​
”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml

Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” 
The change should be rounded to 2 decimal
places."""


def process_coins(drink_order, menu_check, resources_new):
    price = float(MENU[drink]['cost'])
    print(f"Price: ${price}")
    inserted = float(input("please insert coins: "))
    if inserted < price:
        print("Sorry that's not enough money. Money refunded.")
        process_coins(drink_order, menu_check, resources_new)
    else:
        change = round((inserted - price), 2)
        print(f"Here is {change} dollars in change.")
        resources_new["money"] += price
        for keys_l in list(menu_check[drink_order]['ingredients'].keys()):
            resources_new[keys_l] -= menu_check[drink_order]['ingredients'][keys_l]
        return True, resources_new


# Make Coffee.
"""a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink."""


def automat():
    global machine_state, drink
    machine_state = True
    drink = order()
    if drink == "report":
        report(drink_order=drink, resources_c=resources)
        automat()
    elif machine_state == machine_on_off(drink_order=drink):
       if check_resources(drink_order=drink, resources_check=resources, menu_check=MENU):
           process_coins(drink_order=drink, menu_check=MENU, resources_new=resources)
           automat()
    else:
        return


automat()
