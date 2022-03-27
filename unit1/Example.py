# user_data = {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}],
#             'friends': [{'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]},
#                         {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]}]}


# # def get_unique_watched(user_data):
# #     user_watched = user_data
# #     user_watched_movies = []
# #     friends_watched_movies = []
# #     unique_user_movies = []
# #     key_names = ["title"]
    
# #     for item in user_watched["watched"]:
# #         user_watched_movies.append(item[title])

# #     print(len(user_watched_movies))
# #     print(user_watched_movies)
    
# def get_unique_watched(user_data): 
#     friends_movies_1 = user_data["friends"][0]["watched"]
#     friends_movies_2 = user_data["friends"][1]["watched"]
#     all_friends_movie = friends_movies_1 , friends_movies_2
#     watched_movies = user_data["watched"]
#     not_watched = [i for i in all_friends_movie if i not in watched_movies]
#     return not_watched

# print(get_unique_watched(user_data))  
restaurants = []
# print(restaurants[0])
# print(restaurants[0]["rating"])




def get_highest_rated(restaurants):
    my_list = []
    max_rate = None
    highest_rate = None
    for restaurant in restaurants:
        if restaurant["rating"] == []:
            my_list.append(None)
            
            break
        else:
            my_list.append(restaurant["rating"])
        max_rate = max(my_list)

    for restaurant in restaurants:
        if restaurant["rating"] == max_rate:
            highest_rate = restaurant
        
    return highest_rate
    
# max_rate = max(my_list)
# print(max_rate)
# rate_list = []
# for restaurant in restaurants:
#     if restaurant["rating"] == max_rate:
#         rate_list.append(restaurant)
# print(rate_list)
#     
    
print(get_highest_rated(restaurants))

# def get_most_watched_genre(user_data):
#     watched_genre = []
#     most_watched_genre = None
#     for movie in user_data["watched"]:
#         if movie["genre"] == None:
#             return most_watched_genre
#         else:
#             watched_genre.append(movie["genre"])
#         most_watched_genre = max(set(watched_genre), key = watched_genre.count)
#     return most_watched_genre  