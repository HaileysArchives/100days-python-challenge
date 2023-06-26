# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:37:39 2023

@author: kelly
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_age = int(age)

year = int(90 - current_age)

left_days = int(year * 365)
left_weeks = int(year * 52)
left_months = int(year * 12)

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")




