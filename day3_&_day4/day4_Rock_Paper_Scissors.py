# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:47:00 2023

@author: kelly
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

game = [rock, paper, scissors] # list type
# print(game[0])

my_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

my_game = game[my_turn]

random_number = random.randint(0, 2)

# my_rock = (my_game == game[0])
# my_paper = (my_game == game[1])
# my_scissors = (my_game == game[2])

# rock case
if (my_turn == 0) and (random_number == 0):
  print(f"My choose: \n")
  print(rock)
  print(f"Computer choose: \n")
  print(rock)
  print("It's a tied.")
elif (my_turn == 0) and (random_number == 1):
  print(f"My choose: \n")
  print(rock)
  print(f"Computer choose: \n")
  print(paper)
  print("You're lose..😭")
elif (my_turn == 0) and (random_number == 2):
  print(f"My choose: \n")
  print(rock)
  print(f"Computer choose: \n")
  print(scissors)
  print("You're winner✨")

# paper case
if (my_turn == 1) and (random_number == 0):
  print(f"My choose: \n")
  print(paper)
  print(f"Computer choose: \n")
  print(rock)
  print("You're winner✨")
elif (my_turn == 1) and (random_number == 1):
  print(f"My choose: \n")
  print(paper)
  print(f"Computer choose: \n")
  print(paper)
  print("It's a tied.")
elif (my_turn == 1) and (random_number == 2):
  print(f"My choose: \n")
  print(paper)
  print(f"Computer choose: \n")
  print(scissors)
  print("You're loser..😭")

# scissors case
if (my_turn == 2) and (random_number == 0):
  print(f"My choose: \n")
  print(scissors)
  print(f"Computer choose: \n")
  print(rock)
  print("You're lose..😭")
elif (my_turn == 2) and (random_number == 1):
  print(f"My choose: \n")
  print(scissors)
  print(f"Computer choose: \n")
  print(paper)
  print("You're winner✨")
elif (my_turn == 2) and (random_number == 2):
  print(f"My choose: \n")
  print(scissors)
  print(f"Computer choose: \n")
  print(scissors)
  print("It's a tied.")








