import random
import math

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

#Hint 6:Create a function called calculate_score() that takes a List if cards as input and returns the score. 
#Look up the sum() functions to help you do this.

def calculate_score():
    return sum(user_cards), sum(computer_cards)

print(calculate_score())

# Hint 7: Inside calculate_score() check for a blackjack(a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
# 0 will represent a blackjack in our game.

if calculate_score() > 21:


# Hint 8:Inside calculate_score() check for an 11 (ace). If the score is alreay over 21, remove the 11 and replace it with a 1. 
# You might need to look up append() and remove().