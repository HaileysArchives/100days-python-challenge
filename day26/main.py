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
