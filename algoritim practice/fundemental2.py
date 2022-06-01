#Create a function that will tell you whether or not a year is a leap year! How can you tell? Well, 
# if a year is divisible by 4, then it's a leap year.
# But if it is also divisible by 100, then it's not a leap year. 
# Oh unless you are talking about being divisible by 400, then it's a leap year again.

# Example Input: 1976
# Example Output: True

# Example Input: 2014
# Example output: False
year= 2014

def leap_year(year):
    if year % 4 == 0:
        if year % 100==0:
            if year % 400 ==0:
                return True
            else:
                return False
        return True    
    else:
        return False
    
print(leap_year(year))

#************************ EXAMPLE 2 *******************************

#A friend needs a function that will help them count the number of values in an array/list greater than the third index value.

#For every value in the array/list that is greater, print that number also. Finally, return the number of values greater than.

#Example Input: [6,4,5,2,3,7,10,2]
#Examples Output: 6
			#     7
			#    10
			#     3










#Oh dear! Someone at your company messed up the temperature converter app you all sell. 
# Your manager comes to you to fix it. You need to create a function that correctly converts Celsius to Fahrenheit, 
# and then returns the new temperature.

#Chemistry has been a while for a lot of us, so let's review that formula:
#	fahrenheit = (9/5  * celsius) + 32

# Example Input: 30
# Example Output: 86

# Extra Challenge: How would you convert from Fahrenheit to Celsius then? 
# What if the customer wants to choose from which system to convert to?

