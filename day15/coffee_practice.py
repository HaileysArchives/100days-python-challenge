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

# user_menu = input("What would you like? (espresso/latte/cappuccino) ") 


def write_report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"

# 4. Check resources sufficient? 

def check_resources():
    global user_menu
    user_menu = input("What would you like? (espresso/latte/cappuccino) ")

    if user_menu == "report":
        print(write_report())
    elif user_menu == "espresso" or user_menu == "latte" or user_menu == "cappuccino":
        # Rest of the code for preparing the requested menu item
        menu_water = MENU[user_menu]['ingredients']["water"]
        menu_milk = MENU[user_menu]['ingredients']["milk"]
        menu_coffee = MENU[user_menu]['ingredients']["coffee"]

        if resources['water'] < menu_water:
            print("Sorry, there is not enough water.")
        elif resources['milk'] < menu_milk:
            print("Sorry, there is not enough milk.")
        elif resources['coffee'] < menu_coffee:
            print("Sorry, there is not enough coffee.")
        else:
            resources['water'] -= menu_water
            resources['milk'] -= menu_milk
            resources['coffee'] -= menu_coffee
            print(f"Here is your {user_menu}. Enjoy!")

# while True:
#     check_resources()

# # Process coins.
print("Please insert coins.")

quarters_count = input("How many quarters? ")
dimes_count = input("How many dimes? ")
nickles_count = input("How many nickles? ")
pennies_count = input("How many pennies? ")
total = (0.25 * quarters_count) + (0.10 * dimes_count) + (0.05 * nickles_count) + (0.01 * pennies_count)
price = int(MENU[user_menu]['cost'])

change = print(f"Here is ${total - price} in change.")

# 6. Check transaction successful? 
# "Sorry that's not enough money. Money refunded."
# If the user has inserted too much money, the machine should offer change. "Here is $2.45 dollars in change."


