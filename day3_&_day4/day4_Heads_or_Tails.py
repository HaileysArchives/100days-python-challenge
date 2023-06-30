# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:46:05 2023

@author: kelly
"""

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_number = random.randint(0, 1)

if random_number == 1:
    print("Heads")
else: 
    print("Tails")