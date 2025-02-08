#travel log dictionary
# country :  cities_visited, total_visits




travel_log = {
    'United Kingdom' : {
        "cities_visited" : [ 'London', 'Manchester'],
        "number_visits": [2, 1]
    },
    'France' : {
        "cities_visited" : [ 'Paris', 'Frankfurt'],
        "number_visits": [6, 1]
    }
}

print(travel_log['United Kingdom']['cities_visited'][1])