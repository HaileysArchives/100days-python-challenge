# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:48:05 2023

@author: kelly
"""

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = student_scores[0]
count = 0

for score in student_scores:
    count += 1
    if(max_score < student_scores[count - 1]):
        max_score = student_scores[count - 1]
print(f"The highest score in the class is: {max_score}")

