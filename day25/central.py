import pandas

# 모든 데이터는 뉴욕시의 공개데이터 웹사이트 NYC OpenData 사이트에서 찾을 수 있다. 
# (https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(len(gray_squirrels))