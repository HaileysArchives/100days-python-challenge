# List and Dictionary Comprehensions 

# 입력할 양은 줄여주고 코드를 줄여주고 가독성이 좋다.

# For Loop 

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension

numbers_1 = [1, 2, 3]
new_list = [n + 1 for n in numbers_1] # new_list = [new_item for item in list]

name = "Angela"
letters_list = [letter for letter in name] # ['A', 'n', 'g', 'e', 'l', 'a'] 문자열을 개별 문자로 분리해서 새로운 리스트에 추가됨
print(letters_list)

# Predict what new_list will contain. Check your prediction in PyCharm.

double = range(1, 5) # 1, 2, 3, 4
double_list = [n * 2 for n in double]
print(double_list)

range_list = [num * 2 for num in range(1, 5)]

# Conditional List Comprehension => 조건식 추가도 가능
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
names

short_names = [name for name in names if len(name) < 5]
print(short_names)

# Create a new list that contains the names longer than 5 characters in All Caps.
caps_names = [name.upper() for name in names if len(name) >= 5]
print(caps_names)

# Challenge: You are going to write a List Comprehension to create a new list called 'squared_numbers'. This new list should contain every number in the list numbers but each number should be squared. 

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers] # squared_numbers = [num **2 for num in numbers]
print(squared_numbers)

# Challenge: You are going to write a List Comprehension to create a new list called 'result'. This new list should only contain the even numbers from the list numbers.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num % 2 == 0]
print(result)

# Challenge: Take a look inside 'file1.txt' and 'file2.txt'.They each contain a bunch of numbers, 
# each number on a new line. You are going to create a list called 'result' which contains the numbers that are common in both files.

with open("day26/file1.txt") as file1:
    file_1_data = file1.readlines()

with open("day26/file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)