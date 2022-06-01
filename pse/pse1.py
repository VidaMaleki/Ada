#Imagine working on software that deals with restaurant reviews.
#Create a function named get_highest_rated that is responsible for finding the highest-rated restaurant.
#This function should take in a list of dictionaries named restaurants as a parameter.
# Each dictionary represents the data associated with a restaurant, including its rating. 
# This function should have a return value of the restaurant with the highest rating.

restaurants = [{"name": "Grillby's", "rating": 9}, {"name": "Crow's Nest", "rating": 5}]

# def get_highest_rated(restaurants):
#     max_rate = 0
#     highest_rate = None
    
#     for restaurant in restaurants:
#         if restaurants == []:
#             return None
#         elif restaurant["rating"] > max_rate:
#             max_rate = restaurant["rating"]
#             highest_rate = restaurant
#     return highest_rate



def get_highest_rated(restaurants):
    max_rate = 0
    highest_rate = None
    
    for restaurant in restaurants:
        if restaurant["rating"] > max_rate:
            max_rate = restaurant["rating"]
            highest_rate = restaurant
    return highest_rate
print(get_highest_rated(restaurants))