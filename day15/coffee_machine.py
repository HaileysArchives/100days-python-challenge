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

print(MENU['latte']['ingredients']['water'])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(resources['water'])


# 1. Prompt user by asking "What would you like?" (espresso/latte/cappuccino):"

choice = input("What would you like? (espresso/latte/cappuccino) ")


# 2. Turn off the Coffee Machine by entering "off" to the prompt. 
# turn_off = False

on_off = input("Type 'on' if you want it to work or 'off' if you want it to stop working. ")

if on_off == "off":
  coffee_machine = False
elif on_off == "on":
  coffee_machine = True
  

# 3. Print report. 
# Money: $2.5

def report(menu):
  menu = choice
  money = 0
  water = MENU[menu]['ingredients']["water"]
  milk = MENU[menu]['ingredients']["milk"]
  coffee = MENU[menu]['ingredients']["coffee"]
  return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"

print(report(choice))


# 4. Check resources sufficient? "Sorry there is not enough water."

# 5. Process coins.
# quartesrs = $0.25
# dimes = $0.10
# nickles = $0.05
# pennies = $0.01
# => 0.25 + 0.1 * 2 + 0.05 + 0.01 * 2 = $0.52

# 6. Check transaction successful? 
# "Sorry that's not enough money. Money refunded."
# If the user has inserted too much money, the machine should offer change. "Here is $2.45 dollars in change."

# 7. Make Coffee.
# Once all resources have been deducted, tell the user "Here is your latte. Enjoy!"