def a_function(a_parameter):
    a_variable = 15
    return a_parameter

a_function(10)
# print(a_variable) 
# NameError: a_variable은 로컬변수로 해당 항목만이 함수 내에서 사용가능한 유일한 항목이다. 

i = 50 
def foo():
    i = 100
    return i

foo()
print(i)
# 출력결과: 50

def bar():
    my_varibale = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)

bar()
# 16

# 📌 파이썬에는 블록 범위가 없다는 사실 기억하기 if, else, for, while 코드 블록은 외부와 동일


