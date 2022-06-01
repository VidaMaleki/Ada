#From 0 to and including 300, print out any numbers that are multiples of of 3; however, don't print numbers 10, 15, and 21 even if they are.

#What if a user wanted to choose the multiple herself instead of always using 3? How would you change your code?

#Extra Challenge: If you used a for loop for this, change it to a while loop and vice versa. 

for i in range(1,301):
    if i %3 ==0:
        if i== 10 or i == 15 or i == 21:
            continue
        else:
            print(i)
#*********************  EXAMPLE 2 **************************************        
            
#Crow T. Robot needs a way to count how many clusters of tally marks he has. 
# Create a function for him that takes in the number of "tallies" and prints the number of clusters (a grouping of 5 tallies),
# as well as any remainder.

#Example Input: 23
# Example Output: "4 clusters and a remainder of 3 tallies"
# Example Input: 25
# Example Output: "5 clusters"
num = 25
def clusters_of_tally(num):
    clusters= num // 5 
    remaider= num % 5
    if remaider == 0:
        print(f"{clusters} clusters")
    else:
        print(f"{clusters} clusters and remaider is {remaider}")
    
    
clusters_of_tally(num)    
    
    
    
    
#*********************  EXAMPLE 3 **************************************  

#
#You work for a company that sells a countdown clock, but customers are asking for a few additional features and flexibility. 
# Your manager asks you to create a function that would let a customer decide what number the countdown starts at, printing out each number as it counts down.

#But customers also want to select what number to increment the countdown by. 
# Then when it hits 0, customers wish the clock to alert them that, "TIME'S UP!"

#Example Input: start=5, increment=2
#Example Output: 5
			# 3
			# 1
			# TIME'S UP
start = 5
increment = 2
for i in range(start, 0, -increment):
    print(i)
print("TIME'S UP")
