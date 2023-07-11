MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0

def write_report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']} \nMoney: ${money}"


# 6. Process coins.

def process_coins():
    print("Please insert coins.")

    quarters_count = int(input("How many quarters? "))
    dimes_count = int(input("How many dimes? "))
    nickels_count = int(input("How many nickels? "))
    pennies_count = int(input("How many pennies? "))

    global total 
    total = float((0.25 * quarters_count) + (0.10 * dimes_count) + (0.05 * nickels_count) + (0.01 * pennies_count))
    price = float(MENU[user_menu]['cost'])

    left = round((total - price), 2)
    if left >= 0:
        print(f"Here is ${left} in change.")
    else:
        print("")


# 4. Check resources sufficient? 

def check_resources():
    global user_menu
    global money

    user_menu = input("What would you like? (espresso/latte/cappuccino) ")

    if user_menu == "report":
        print(write_report())
    elif user_menu == "espresso" or user_menu == "latte" or user_menu == "cappuccino":
        # Rest of the code for preparing the requested menu item
        menu_water = MENU[user_menu]['ingredients']["water"]
        menu_milk = MENU[user_menu]['ingredients']["milk"]
        menu_coffee = MENU[user_menu]['ingredients']["coffee"]
        global menu_cost
        menu_cost = float(MENU[user_menu]["cost"])
        
        process_coins()

        if resources['water'] < menu_water:
            print("Sorry, there is not enough water.")
        elif resources['milk'] < menu_milk:
            print("Sorry, there is not enough milk.")
        elif resources['coffee'] < menu_coffee:
            print("Sorry, there is not enough coffee.")
        elif total >= menu_cost:
            resources['water'] -= menu_water
            resources['milk'] -= menu_milk
            resources['coffee'] -= menu_coffee
            money += menu_cost
            print(f"Here is your {user_menu}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


while True:
    check_resources()



