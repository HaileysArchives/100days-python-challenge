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

import pandas

data = pandas.read_csv("day25/weather_data.csv") # read csv file. (Just one step code)
print(data)
print(data["temp"]) # 열의 이름을 지정하면 데이터를 찾는 방법을 자동적으로 알 수 있다. 