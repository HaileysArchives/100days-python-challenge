import pandas

import os 
print(os.getcwd())

data = pandas.read_csv("day25/weather_data.csv") # read csv file. (Just one step code)
# print(data)
# print(data["temp"]) # 열의 이름을 지정하면 데이터를 찾는 방법을 자동적으로 알 수 있다. 

# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
# # print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge: Convert Monday's temperature to Fahrenheit

# convert_temp = (monday.temp * 1.8) + 32
# print(convert_temp) 

monday_temp = int(monday.temp)
monday_temp_F = (monday_temp * 9/5 + 32)
print(monday_temp_F)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [73, 43, 92]
}

data2 = pandas.DataFrame(data_dict)
print(data2) # 딕셔너리의 값을 사용해서 표가 만들어진다 

data2.to_csv("day25/new_data.csv") # Convert CSV file. 
