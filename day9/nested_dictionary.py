
#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

#Nesting
capitals = {
	"France": "Paris",
	"Germany": "Berin",
}

#Nesting a List in a Dictionary

# travel_log = {
#	"France": "Paris", "Lille", "Dijon"
#} => Error : Each key can only have one value!!!

travel_log = {
	"France": {"cities_visited": ["Paris", "Lille", "Digon"], "total_visits": 12},
	"Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

