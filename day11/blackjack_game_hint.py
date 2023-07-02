import random
import math
import os 
# import art

def deal_card(): 
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

user_cards = []
computer_cards = []

for _ in range(1):
    new_card = deal_card() #have output
    user_cards.append(new_card)
    computer_cards.append(new_card)

# user_cards += new_card => warning!!! (typeerror) => actually the same .extend() function. 
# user_cards.extend(new_card) => how to .expend() function? It needs list type. so we change the "new_card = [deal_card()]" that is correct. but we only want single item, not a list, .append() functions use possible. 

user_cards.append(deal_card())
computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

#Hint 6: Create a function called calculate_score() that takes a List if cards as input and returns the score. 
#Look up the sum() functions to help you do this.

def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0

# Hint 7: Inside calculate_score() check for a blackjack(a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
# 0 will represent a blackjack in our game.


# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is alreay over 21, remove the 11 and replace it with a 1. 
# You might need to look up append() and remove().

    if (11 in cards) and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

# Hint 9: Call calculate_score(). If the computer of the user has a blackjack (0) or if the user's score is over 21, then the game ends.

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or computer_score == 0 or user_score > 21:
    end_game = True
    print("Game over.")

# Hint 10: If the game has not ended, ask the user if they want to draw another card. 
# If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

draw = input("You wanna draw another card? 'yes' or 'no. ")
if draw == "yes":
    deal_card()
    draw_card = deal_card()
    user_cards.append(draw_card)
elif draw == "no":
    end_game = True
    print("Game over.")

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

user_score = calculate_score(user_cards) # rechecked 

if user_score == 0 or computer_score == 0 or user_score > 21:
    end_game = True
    print("Game over.")

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

if computer_score < 17:
    deal_card()
    draw_card = deal_card()
    computer_cards.append(draw_card)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare():
    if computer_score == user_score:
        print("A draw.")
    elif computer_cards == 0 or computer_cards == 11 or computer_score > 21:
        print("User's lose. The Dealer's win.")
    elif user_cards == 0 or user_cards == 11 or user_score > 21:
        print("The Dealer's lose. You win.")

compare()

#Hint 14: Ask the user if they want to restart the game. 
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

restart = input("You wanna restart the game? 'yes' or 'no. ")

if restart == "yes":
    os.system('cls')
    # blackjack()
    # print(art.logo)
elif restart == "no":
    print("The end game.")