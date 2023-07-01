import random

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #type = "list"

# 1. The user and computer should each get 2 random cards.

user_card = random.sample(cards, 2) #sapmle 함수로 리스트에서 2개 랜덤 추출
computer_card = random.sample(cards, 2)

# 2. Add up the user's and the computer's scores.

user_score = int(user_card[0] + user_card[1])
computer_score = int(computer_card[0] + computer_card[1])

print(user_card)
print(computer_card)

# 3. Does the user of computer have a blackjack? (ace + 10) => win / lose
if user_card[0] == 11 or user_card[1] == 11 or computer_card[0] == 11  or computer_card[1] == 11:
    if user_score < computer_score:
        print("Dealer's win.")
    elif user_score > computer_score:
        print("User's win.")
    else:
        print("A draw.")

# 4. Is user's score over 21? => Do they have and "ace"? 
# If they have an "ace", if the ace counts as a 1 insteads 11, are they still over 21?

def over_21():
    if user_score > 21:
        if user_card[0] == 11:
            choose = input("You wanna ace card 1 instead 11? yes or no? ")
            if choose == "yes":
                user_card[0] = 1
                print(f"You change the ace card number {user_card[0]}.")
                if (user_card[0] + user_card[1]) > 21:
                    print("You're lose.")
        elif user_card[1] == 11:
            choose = input("You wanna ace card 1 instead 11? yes or no? ")
            if choose == "yes":
                user_card[1] = 1
                print(f"You change the ace card number {user_card[1]}.")
                if (user_card[0] + user_card[1]) > 21:
                    print("You're lose.")

over_21()

# 5. Ask the user if they want to get another card. And draw another card.

ask = input("You pick the another card? 'yes' or 'no'. ")

if ask == "yes":
    user_another_card = random.choice(cards)
    print(f"Another card is {user_another_card}.")
elif ask == "no":
    over_21()
    
# 6. Computer plays, if score is less than 17, keep drawing cards.