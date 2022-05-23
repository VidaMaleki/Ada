red = [50, 43, 25, 72]
blue = [25, 36, 43, 50, 80]

def get_intersection(red, blue):
    new_dict= {}
    for i , j in enumerate(sorted(red)):
        if j in blue:
            new_dict[i] = j
    return list(new_dict.values())


print(get_intersection(red, blue))