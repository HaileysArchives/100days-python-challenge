from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

#Empty_dictionary
auction_users = {}

#Just one
print("Welcome to the secret auction program.")

end_game = True

while end_game:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    direction = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    highest_price = 0

    if direction == "yes":
        for key in auction_users:
            auction_users[name] = price
            clear()
    elif direction == "no":
        for key in auction_users:
            highest_price = max(auction_users[key])
        print(f"The winner is {name} with a bid of ${highest_price}.")
