# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:48:48 2023

@author: kelly
"""

#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for letter in range(1, nr_letters + 1):
#     letter = random.randint(0, len(letters) - 1)
#     print(letters[letter], end='')  # 붙여쓰기 (end = '')

# for symbol in range(1, nr_symbols + 1):
#     symbol = random.randint(0, len(symbols) - 1)
#     print(symbols[symbol], end='')

# for number in range(1, nr_numbers + 1):
#     number = random.randint(0, len(numbers) - 1)
#     print(numbers[number], end='')

# for letter in range(1, nr_letters + 1):
#     letter = random.randint(0, len(letters) + 1)
#     print(letters[letter], end='')  # 붙여쓰기 (end = '')

#     for symbol in range(1, nr_symbols + 1):
#         symbol = random.randint(0, len(symbols) + 1)
#         print(symbols[symbol], end='')

#         for number in range(1, nr_numbers + 1):
#             number = random.randint(0, len(numbers) + 1
# => IndexError: list index out of range => The reason is
"""
위 코드에서는 letters, numbers, symbols의 인덱스를 벗어나 출력하려고 했기 때문에 IndexError가 발생합니다. 리스트의 인덱스는 0부터 시작하며, len() 함수로 호출되는 리스트의 길이는 실제 원소 개수보다 1 크기 때문입니다. 

 예를 들어, letters 리스트의 길이는 26이지만 인덱스는 0부터 25까지입니다. 이를 수정하려면, random.randint(0, len(letters) - 1) 과 같이 -1을 해주면 됩니다. 

 또한, for문에 range(start, end)를 사용할 때 end는 포함되지 않으므로, range(1, nr_letters + 1)과 같이 범위를 설정해야 합니다."""

# for x in range(0, 3): # use thonny how to use
#     for y in range(0, 4):
#       for z in range(0, 5):
#         print(z)

# ========================================================================
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# passward = list()

# for letter in range(1, nr_letters + 1):
#     letter = random.randint(0, len(letters) - 1)
#     passward.append(letters[letter])

# for symbol in range(1, nr_symbols + 1):
#     symbol = random.randint(0, len(symbols) - 1)
#     passward.append(symbols[symbol])

# for number in range(1, nr_numbers + 1):
#     number = random.randint(0, len(numbers) - 1)
#     passward.append(numbers[number])

# rand_number = random.randint(0, len(passward) - 1)
# =========================================
password = []

# Append letters, symbols, and numbers to passward list
for letter in range(1, nr_letters + 1):
    letter_index = random.randint(0, len(letters) - 1)
    password.append(letters[letter_index])

for symbol in range(1, nr_symbols + 1):
    symbol_index = random.randint(0, len(symbols) - 1)
    password.append(symbols[symbol_index])

for number in range(1, nr_numbers + 1):
    number_index = random.randint(0, len(numbers) - 1)
    password.append(numbers[number_index])

random.shuffle(password)

password_string = "".join(password)
print(password_string)

count = 0

# count the password number.
for word_number in password:
    count += 1
print(count)

# Shuffle the passward list
# for i in range(len(passward)):
#     j = random.randint(0, i)
#     passward[i], passward[j] = passward[j], passward[i]

# print(passward)
