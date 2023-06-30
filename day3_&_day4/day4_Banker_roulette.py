# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:46:24 2023

@author: kelly
"""

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
# print(len(names))

number = len(names)
rand_number = random.randint(0, number)
# print(type(rand_number))

random_name = (names[rand_number - 1])
print(f"{random_name} is going to buy the meal today!")
