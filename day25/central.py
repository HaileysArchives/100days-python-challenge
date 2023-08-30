import pandas

# 모든 데이터는 뉴욕시의 공개데이터 웹사이트 NYC OpenData 사이트에서 찾을 수 있다. 
# (https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]

gray_squirrels_count = len(gray_squirrels)
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict) # 데이터프레임으로 초기화시켜주어야 한다
df.to_csv("day25/squirrels_count.csv")