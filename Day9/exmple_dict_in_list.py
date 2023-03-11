## travel_log is List and inside that Dictionary and for cities again for key=cities - it value is defined as list []

travel_log = [
    {
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
        },
    {
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(countries_visited,times_visited,cities_visited):
    new_country = {}
    new_country["country"] =   countries_visited
    new_country["visits"]  =   times_visited
    new_country["cities"]  =   cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)
add_new_country("India", 5, ["Bangalore", "Agra","Delhi","Pune"])
print(travel_log )