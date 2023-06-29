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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# def add_new_country(new_country, new_visits, new_cities):
#     for i in travel_log:
#         travel_log[i + 2][country] = new_country
#         travel_log[i + 2][visits] = new_visits
#         travel_log[i + 2][cities] = new_cities

def add_new_country(new_country, new_visits, new_cities):
    new_entry = {
        "country": new_country,
        "visits": new_visits,
        "cities": new_cities
    }
    travel_log.append(new_entry)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
