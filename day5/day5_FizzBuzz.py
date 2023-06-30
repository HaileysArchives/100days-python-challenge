# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:48:33 2023

@author: kelly
"""

#Write your code below this row 👇

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 ==0):
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif (number % 3 == 0):
        print("Fizz")
    else:
        print(number)
 