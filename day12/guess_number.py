from art import logo
import random

print(logo)
print("Welcome to the Number Guess Game! \nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)
use_guess = []

def compare():
    if guess == answer:
        print("correct.")
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")

if difficulty == "hard":
    for i in range(0, 5):
        guess = int(input("Make a guess: "))
        use_guess.append(guess)

        compare()

    if use_guess[4] != answer:
        print("You're lose.😭")

elif difficulty == "easy":
    for i in range(0, 10):
        guess = int(input("Make a guess: "))
        use_guess.append(guess)
        
        compare()
    
    if use_guess[9] != answer:
        print("You're lose.😂") 

else:
    print("You don't write 'easy' or 'hard'. Please write again.")