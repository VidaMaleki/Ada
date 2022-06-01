
#Imagine working on software that processes lists of numbers. 
# Create a function named merge_lists that takes two sorted lists and merges them into a single sorted list. 
# This function should take in two lists of whole numbers. 
# The function should return a new sorted list which consists of the elements of the two arguments.


list1 = [1, 2, 4, 5]

list2 = [-30, -10, 0, 15, 16]
print(list1[:])

def merge_lists(list1, list2):
    i = len(list1)-1
    j = len(list2)-1
    k = i+j +1
    list1[len(list1):] = list2[:len(list2)]
    while k >=0:
        if i>=0 and j>=0 and list2[j] <=  list1[i]:
            list1[k] = list1[i]
            i -= 1
        elif j>=0:
            list1[k] = list2[j]
            j-=1
        k -= 1
    return list1

def merge_lists(list1, list2):
    merged_list = list1 + list2
    sorted_list = []
    while merged_list:
        min_num = merged_list[0]
        for num in merged_list:
            if num < min_num:
                min_num = num
        sorted_list.append(min_num)
        merged_list.remove(min_num)
    return sorted_list   




# print(merge_lists(list1, list2))


