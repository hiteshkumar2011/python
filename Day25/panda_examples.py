import  pandas
import  math
#data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#print (type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print((data_dict))

#temp_list = data["temp"].to_list()

# length = (len(temp_list))
# total = sum(temp_list)
# avg_temp = total / length
# temp = "{:.2f}".format(avg_temp)
# print(data["temp"].mean())
# print(f" The average temperature is: {temp}")
#
# print("The max temperature is:",data["temp"].max())
# print(data["condition"])
#print(data.condition)

#print(data[data.day == "Monday"])
# max_temp = data["temp"].max()
# highest_temp = data[data.temp >= max_temp]
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday)
#print(monday.condition)
monday_temp_F = float(monday.temp * 1.8) + 32
# print(monday_temp_F)


# Create a DataFrame from Scratch

data_dict = {
        "students": ["Amy", "James","HKT"],
        "scores": [76,85, 64]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("new_dataframe.csv")





