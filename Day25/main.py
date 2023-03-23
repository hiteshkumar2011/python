import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_color = (data[data["Primary Fur Color"] == "Gray"])
red_squirrels =   (data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels =    (data[data["Primary Fur Color"] == "Black"])

gray_squirrels_count = len((data[data["Primary Fur Color"] == "Gray"]))
red_squirrels_count = len((data[data["Primary Fur Color"] == "Cinnamon"]))
black_squirrels_count = len((data[data["Primary Fur Color"] == "Black"]))

print(black_squirrels_count)
print((red_squirrels_count))
print(gray_squirrels_count)

squirrels_data_dic = {
                     "Fur Color": ["Gray","Red","Black"],
                     "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]

}
df = pandas.DataFrame(squirrels_data_dic)
df.to_csv("squirrel_count.csv")
#print(squirrels_data_dic)