array = [10, 12, 11, 15]
low = 10
high = 15
# o(n + m)  or o(n)
def get_missing_numbers_in_range(array, low, high):
    hash_nums = {}
    for num in array: #o(n)
        hash_nums[num] = True

    missing_nums = []
    for num in range(low, high): #o(m)
        if num not in hash_nums: #o(1)
            missing_nums.append(num)

    return missing_nums


def test_get_missing_numbers_in_range():
    assert get_missing_numbers_in_range([10, 12, 11, 15], 10, 15) == [13, 14]


def test_get_missing_numbers_in_range_small_range():
    assert get_missing_numbers_in_range(
        [1, 14, 11, 51, 15], 50, 55) == [50, 52, 53, 54]
    
#another solution but with time complexcity o(n*m) or o(n^2)
# def get_missing_numbers_in_range(array, low, high):
#     missing_nums = []

#     for i in range(low, high): #o(m)
#         if i not in array: #o(n)
#             missing_nums.append(i) 

#     return missing_nums