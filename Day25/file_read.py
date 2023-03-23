## Reading CSV data
import csv

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    #print(data)
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


