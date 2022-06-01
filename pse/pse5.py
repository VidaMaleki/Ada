#Imagine working on software that processes lists of numbers. 
# Create a function named pairs_with_given_sum It finds the number of pairs of numbers in a list which add up to a given target. 
# This function should take in a list of whole numbers and a target as parameters. 
# This function should have a return value of the integer of number of pairs.

numbers = [97, 51, 49, 35, 3, 65, 25, 35,51]
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

def pairs_with_given_sum(numbers, target):
    count = 0
    pair_list = []
    for i in numbers:
        pair = target - i
        if pair in numbers:
            count +=1
            pair_list.append(i)
    print(pair_list)
    return count //2

print(pairs_with_given_sum(numbers, target))