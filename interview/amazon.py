#Given a string s containing only characters '(' and ')' determine if the input string is valid.
# The string is valid if every open bracket has a matching closed bracket. 
# When finished, consider cases where there are two types of brackets in the string.

valid_string = "[[([{])]]"

def is_nested_parens(parens):
    par_dict= {'(' : ')', '[': ']', '{': '}'}
    stack = []
    for par in parens:
        if par in par_dict:
            print(par)
            stack.append(par_dict[par])
            print(par_dict[par])
            print(stack)
        elif len(stack) > 0 and par == stack[-1]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


def isValid(sequence ):

    while True:
        if '()' in sequence :
            sequence = sequence.replace ( '()' , '' )
        elif '{}' in sequence :
            sequence = sequence.replace ( '{}' , '' )
        elif '[]' in sequence :
            sequence = sequence.replace ( '[]' , '' )
        else :
            return not sequence
                
print(isValid(valid_string))
    


#"given a list of nums, print a list of the duplicates that appear in the list"



nums = [1, 2, 3, 2, 3, 7, 5, 9, 1]
def dupplicate(nums):
    new_list = []
    duplicates = []
    for num in nums:
        if num in new_list:
            duplicates.append(num)
        else:
            new_list.append(num)
    return duplicates

print(dupplicate(nums))



#Given an array of integers (both positive and negative) and a target sum,
#find all unique pairs in the array that add to the sum.
#EX input: [1, 3, 2, 2, 2, -1, 5, 0, 9, 4, 3, 2], 4
#EX output: {(1, 3), (2, 2), (-1, 5), (0, 4)}
#Output pairs in a set of tuples. (I initially thought dictionary and clarified that that was what he wanted, and he said yes.
# I later identified it was a set, not a dict, to which he also said yes)
nums = [1, 3, 2, 2, 2, -1, 5, 0, 9, 4, 3, 2] 
target = 4
def find_pair(nums, target):
    pairs = {}
    answer = set()
    for index, num in enumerate(nums):
        second = target - num 
        if second in pairs:
            answer.add((nums[pairs[second]], num))
        pairs[num] = index
    return answer       
print(find_pair(nums, target))    


#### Whole Foods has an app that allows customers to order their groceries online. 
# They would like to add a feature to the app that shows customers how many items they have in their shopping cart. 
# ### Write a method called count_shopping_cart, which takes in a list of items and prints out how many times each item occurs in the list.
list1 = ["a", "b", "c", "c", "d", "a"]
def count_shopping_cart(list1):
    count_items = {}
    for i in list1:
        count_items[i] = count_items.get(i, 0) +1
    return count_items

print(count_shopping_cart(list1))

#Given an array of integers and an integer denoting a sum, create a function that returns the indeces of the pairs of integers that equate to the sum given.
integers= [1, 2, 3 , 3, 4] 
target = 6 
#Output: [1,3].
# After writing solution, was asked about the space/time complexity and how to imporve them.

def indecies(integers,target ):
    answer = {}
    result = []
    for i , j in enumerate(integers):
        d = target - j
        if d in answer:
            result.append((answer[d], i))
        answer[j] = i
    return result      
print(indecies(integers,target ))
#Given two strings A and B, output if A is present in B.
#For ex: if A is “cat", and B is “carrot” - the output should be true
#if A is “cat” and B is “actor” - the output should be false

a = "cat"
b = "carrot"

def split_string(a):
    list1 = list(str(a))
    return list1

def match_a_b(a, b):
    new_list = []
    list1 = split_string(a)
    list2 = split_string(b)
    for i in range(len(list2)):
        if list2[i] in list1:
            new_list.append(list2[i])
    if "".join(new_list) == a:
        return True
    return False

print(match_a_b(a, b))

#I have two collections of numbers that are sorted in descending order,
# and want a function that will give me the merged collection of the two, 
# still sorted in descending order. What is time complexity of your solution?



#given a string, return True if the string is a palindrome,
# False if it's not. Function should be case insensitive, 
# ignore whitespace and punctuation. Provided sample input.


#Two sum! want the indexes of the 2 numbers returned and there are multiple pairs, 
# so want each pair as it's own list. So return a list of lists,
# with each inner list being a 2 item pair of the indexes

#given a string return the first letter of each word. Input:
# "Hello, World" output HW - he just told me the question, it wasnt on replit or given
sentence = "Hello, World"
def sentence_split(sentence):
    word = sentence.split(" ")
    initial = ""
    for letter in word:
        initial += letter[0]
    return initial
print(sentence_split(sentence))

#given a list of strings return the dupicates. inputs = ["hi", "hi","test","this"] output: ["hi"]



#Given a list of full names (first and last), return a list of just the first names. If there are multiple people who share the same first name, return the first name with the initial of the last name
#input = ['Nina Lane','Nina Jeong', 'Ada Lovelace', 'Jared Stewart']
# output will be Nina L, Nina J, Ada, Jared

