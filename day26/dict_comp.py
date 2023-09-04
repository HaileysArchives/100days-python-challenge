# Dictionary Comprehension 

# new_dict = {new_key:new_value for item in list} # 가장 단순한 형태의 딕셔너리 컴프리헨션

# 혹은 이미 존재하는 딕셔너리에 있는 값을 가지고 새로운 딕셔너리를 만들 수도 있다
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test} # 조건식 추가

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
students_scores = {student:random.randint(1, 100) for student in names}

# students_scrore = {
#     "Alex": 89,
#     "Beth": 98 
# }

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)








