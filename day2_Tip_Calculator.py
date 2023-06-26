# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:37:56 2023

@author: kelly
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Welcome to the tip calculator.
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93

print("Welcome to the tip calculaor.")

total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

c_result = round(((total * (1 + (tip_percentage / 100))) / people) , 2)

print(f"Each person should pay: ${c_result}")



