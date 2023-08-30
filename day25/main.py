# Day 25: Working with CSV files and Analysing Data with Pandas 

# Open the weather_data.csv file. 
# Use readlines() to create a list named data that contains the values from the csv file.

import os 
print(os.getcwd())

# with open("day25/weather_data.csv") as data_file:
#     weather_data = data_file.readlines() # List 
#     print(weather_data)

# 파이썬에는 csv 파일을 지원하는 라이브러리가 내장되어 있다. => import csv

import csv 

with open("day25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1])) # Convert integer type. 
    print(temperatures) 


# 위의 import csv를 사용해서 쓴 긴 줄의 코드를 import pandas를 이용해서 코드의 길이를 훨씬 줄일 수 있다. 
import pandas

data = pandas.read_csv("day25/weather_data.csv") # read csv file. (Just one step code)
print(data)
print(data["temp"]) # 열의 이름을 지정하면 데이터를 찾는 방법을 자동적으로 알 수 있다. 

data_dict = data.to_dict() # 딕셔너리 유형으로 변환 
print(data_dict) 

temp_list = data["temp"].to_list() # 파이썬의 원시 데이터 형태 (리스트 타입)
print(len(temp_list))

# Challenge: Calculate the average temperature.

temp_sum = sum(temp_list)
print(f"average: {temp_sum / len(temp_list)}")

# average = sum(temp_list) / len(temp_list) 
# print(average)

# Method mean (average) 
print(data["temp"].mean()) 

# print(max(data["temp"]))
print(data["temp"].max())

# Get Data in Columns (열을 선택하는 방법)
print(data["condition"]) 
print(data.condition) # 판다스가 각각의 열과 칼럼명을 가져가서 속성값으로 변환하기 때문에 이전 방식과 같은 결과값을 출력한다

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data["day"] == "Monday"])

# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
print(data[data.temp == data.temp.max()])