# file = open("my_file.txt") # nothing's happening.
# contents = file.read()
# print(contents) # 읽은 내용 인쇄 
# file.close()

# Why do we need to do close the file? 

# with open("my_file.txt") as file: # as로 간단하게 이름 짓기 (Keyword)
#     contents = file.read()
#     print(contents)
#     file.close()

# 키워드로 우리는 더이상 파일을 닫는 것을 기억할 필요가 없다. 

import os

currentPath = os.getcwd() # Get the current working directoey (cwd)

print(currentPath) # print path
os.chdir(currentPath) # change path


with open("my_file.txt") as file:
    file.write("New text.") # Error : 파일을 읽기 전용 모드로 열었기 때문 


