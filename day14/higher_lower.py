import random 
from game_data import data
from art import logo, vs

# for person in data:
#         compare = 0
#         compare = print(f"Compare A: {person.name}, {person.description}, {person.country}")

print(logo)

a = random.choice(data)
# print(a["name"])

# name = a["name"]
# follower_count = a["follower_count"]
# description = a["description"]
# country = a["country"]

end_game = False
score = 0

def play_game(): 
    global a
    b = random.choice(data)
    global score
    
    compare_A = print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(vs)
    compare_B = print(f"Against B: {b['name']}, {b['description']}, {b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    a_followers = a['follower_count']
    b_followers = b['follower_count']
    
    if user_choice == 'A' or user_choice == 'a':
        if a_followers > b_followers:
            score += 1
            print(f"You're right! Current score: {score}")

        elif a_followers < b_followers:
            print(f"Sorry, that's wrong. Final score: {score}")

    elif user_choice == 'B' or user_choice == 'b':
        if a_followers > b_followers:
            print(f"Sorry, that's wrong. Final score: {score}")
        elif a_followers < b_followers:
            score += 1
            print(f"You're right! Current score: {score}")

    a = b

# a = b
# print(a['name'])

while not end_game:
    play_game()    


