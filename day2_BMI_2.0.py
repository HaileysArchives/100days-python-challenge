# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:38:39 2023

@author: kelly
"""

import os
os.rename('day2_BMI_2.0.py', 'day3_BMI_2.0.py')

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(float(weight / (height ** 2)))

if (BMI < 18.5):
    print(f"Your BMI is {BMI}, you are underweight.")
elif (BMI > 18.5 and BMI <= 25):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif (BMI > 25 and BMI <= 30):
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif (BMI > 30 and BMI <= 35):
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.") 