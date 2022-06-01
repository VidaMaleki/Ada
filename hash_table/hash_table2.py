pairs = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]



def get_symmetric_pairs(pairs):
    hash_map = {}
    new_list = []
    for i in range(len(pairs)):
        first = pairs[i][0]
        second = pairs[i][1]
        if (second in hash_map.keys() and hash_map[second] == first):
            new_list.append([second, first])
        else:
            hash_map[first] = second
    return new_list
print(get_symmetric_pairs(pairs))    


# def get_symmetric_pairs(pairs):
#     pairs_map = {}

#     for pair in pairs:
#         pairs_map[pair[0]] = pair[1]

#     symmetric_pairs = []

#     for pair in pairs:
#         key, val = pair[0], pair[1]
#         if pairs_map.get(val) == key:
#             symmetric_pairs.append([key, val])
#             pairs_map.pop(key)

#     return symmetric_pairs