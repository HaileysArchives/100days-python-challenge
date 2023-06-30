# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:46:40 2023

@author: kelly
"""

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# # int_position = position.split("")
# # print(type(int_position))
# # print(int_position[0])

# plist = position.split()
# # print(type(plist))

# map_row = int(plist[0]) - 1
# map_column = int(plist[1]) - 1

# print(map[map_row][map_column])

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

int_column = int(position[0]) - 1
int_row = int(position[1]) - 1
map[int_row][int_column] = 'x'

print(f"{row1}\n{row2}\n{row3}")