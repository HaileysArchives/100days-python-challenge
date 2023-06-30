# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:47:44 2023

@author: kelly
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
sum = 0
average = 0

for x in student_heights:
    count += 1
    sum += x
    average = sum / count
print(round(average)) 
    
    



