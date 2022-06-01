def is_permutation(str1, str2):
    dict_1 = {}
    for letter in str1:
        if letter in dict_1:
            dict_1[letter] += 1
        else:
            dict_1.setdefault(letter, 1)

    for letter in str2:
        if letter in dict_1:
            if dict_1[letter] == 1:
                del dict_1[letter]
            else:
                dict_1[letter] -= 1
        else:
            return False

    return len(dict_1) == 0