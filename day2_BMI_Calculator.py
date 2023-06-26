# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:37:14 2023

@author: kelly
"""

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height))
h = float(height)
w = float(weight) 

BMI = (w / (h**2))

print(int(BMI))

