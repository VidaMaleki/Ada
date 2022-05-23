numbers = [97, 51, 49, 35, 3, 65]
target = 100

def pairs_with_given_sum(numbers, target):
    hash_nums = {}
    count = 0
    if not numbers:
        raise ValueError("Empty List")
    for index, num in enumerate(numbers):
        if type(num) != int: 
            raise TypeError("Input must be integer")
        diff = target - num
        if diff in hash_nums:
            count += 1
        hash_nums[num] = index
    return count

print(pairs_with_given_sum(numbers, target))