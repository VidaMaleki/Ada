def is_palindrome_permutation(s):
    if len(s) == 0:
        return True
    d = {}
    odd_matches_count = 0
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for val in d.values():
        odd_matches_count += val % 2
    return odd_matches_count < 2


