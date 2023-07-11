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
}

user_menu = input("What would you like? (espresso/latte/cappuccino) ")


def write_report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"


def check_resources():
    if user_menu == "report":
        print(write_report())
    else:
        # Rest of the code for preparing the requested menu item
        menu_water = MENU[user_menu]['ingredients']["water"]
        menu_milk = MENU[user_menu]['ingredients']["milk"]
        menu_coffee = MENU[user_menu]['ingredients']["coffee"]

        if resources['water'] < menu_water:
            return "Sorry, there is not enough water."
        elif resources['milk'] < menu_milk:
            return "Sorry, there is not enough milk."
        elif resources['coffee'] < menu_coffee:
            return "Sorry, there is not enough coffee."
        else:
            return f"Here is {user_menu}. Enjoy!"

print(check_resources())

