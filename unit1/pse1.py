restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]

def get_highest_rated(restaurants):
    max_rate = 0
    highest_rate = None
    
    for restaurant in restaurants:
        if restaurants == []:
            return None
        elif restaurant["rating"] > max_rate:
            max_rate = restaurant["rating"]
            highest_rate = restaurant
    return highest_rate

print(get_highest_rated(restaurants))