#Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
#Find the kth positive integer that is missing from this array.

arr = [2,3,4,7,11]
k = 5

def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''
    missing_nums = []
    new_range = max(numbers) + k + 1
    
    for i in range(new_range):
        if i not in numbers:
            missing_nums.append(i)
    return missing_nums[k]

print(kth_missing_positive_number(arr, k))










def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of numbers in increating order & a positive integer k
    OUTPUT: The kth missing number'''
    
    expected = 1
    missing_count = 0
    
    for number in numbers:
        while expected != number:
            missing_count += 1
            if missing_count == k:
                return expected
            expected += 1
            
    while missing_count < 1:
        expected += 1
        missing_count +=1
        
    return expected
