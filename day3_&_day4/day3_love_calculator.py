# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:45:09 2023

@author: kelly
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 =name1.lower()
name2 = name2.lower()

first_count = 0
second_count = 0

true1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
true2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

love1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

first_count = true1 + true2
second_count = love1 + love2

score = str(first_count) + str(second_count)
iscore = int(score)
# print(type(score))

if iscore < 10 or iscore > 90:
    message = "you go together like coke and mentos."
    print(f"Your score is {iscore}, {message}")
elif iscore >= 40 and iscore <= 50:
    message = "you are alright together."
    print(f"Your score is {iscore}, {message}")
else:
    print(f"Your score is {iscore}.")

