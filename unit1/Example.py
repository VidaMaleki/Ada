#- each booking for specific number of nights and indicates whether a bath is included or not
#- overnight stays cost $50 per night
#- A bath costs $30
# the funstion accepts two lists:
#   - overnight_reservations, a list of integers where each integer represents the number of overnight stays a single customer booked.
#   - bath_booked, a list of boolean values where each boolean indicates whether a bath was included in booking for that customer(True) or not(False)
#the program should report each of the following by printing:
#   - a summary of earnings for each customer
#   - the total earnings from all customers
#   - the total earned from all baths
#
#Example -1
# overnight_reservations = [3, 1, 5]
# bath_booked = [False, True, True]

#example output 
#Welcome to Ada's Doggy Getaway!
#Customer 1 spent $150
#Customer 2 spent $80
#Customer 3 spent $280
#Combined all customers paid $510 total
#The total spent on baths was $60

#Example -2
#overnight_reservations = [3]
#bath_booked = [False]

#Welcome to Ada's Doggy Getaway!
#Customer 1 spent $150
#Combined all customers paid $150 total
#The total spent on baths was $0


#part 2 handeling ties

#the function should now also report the following by printing:
#   - the highest total spent by single customer
#   - and when there are multiple customers who are tied for spending the highest amount, print all of thoes customers

#Example
# overnight_reservations = [3, 0, 3]
# bath_booked = [True, True, True]

#example output 
#Welcome to Ada's Doggy Getaway!
#Customer 1 spent $180
#Customer 2 spent $30
#Customer 3 spent $180
#Combined all customers paid $390 total
#The total spent on baths was $90

#$180 was the most paid by any single customer
#The customer(s) that paid the most were: 1, 3

# part 3 Going beyound
# how can we update the solution if the pet hotel now offers nail trims and a discount for booking 5 nights or more?

#- Nail trim costs $15
#- if a customer books 5 night or more then each night is $45, instead of $50
#_ the function now accept three lists:
#   - overnight_reservation
#   - bath_booked
#   - nail_trim_booked

#the function should report the following after adjusting calculations according to the values outlined above by printing:

# A summary of earnings for each customer
# the total earnings from all customers
#The total earned from all baths
#The highest total spent by a single customer
# when there are multiple customers who are tied for spending the highest amount, print all of thoes customers
# And the total earned from all bathes and all nail trims combined

overnight_reservations = [3, 1, 3]
bath_booked = [True, True, True]
bath = 30
overnigh_stay = 50



def ada_doggy_getaway(overnight_reservations, bath_booked ):
    print("Welcome to Ada's Doggy Getaway!")
    report()
        

def overninght_reserve(customer_id):
    cost = overnight_reservations[customer_id] * overnigh_stay
    return cost

def bath_reserve(customer_id):
    cost = 0
    if bath_booked[customer_id] == True:
        cost = 1 * bath
    return cost

def total_bath():
    total = 0
    for customer in range(len(overnight_reservations)):
        total += bath_reserve(customer)
    return total

def earning_per_customer(customer_id):
    earning = overninght_reserve(customer_id) + bath_reserve(customer_id)
    return earning

def total_earnings():
    total = 0
    for customer in range(len(overnight_reservations)):
        total += earning_per_customer(customer)
    return total

def most_paid():
    most_dict = {}
    for customer in range(len(overnight_reservations)):
        most_dict[customer] = earning_per_customer(customer)
    return most_dict    

def most_spent_customers():
    max_value = max(most_paid().values())
    max_keys = [customer for customer, spent in most_paid().items() if spent == max_value]
    #index starts from zero however ranks start from one and we are looking for rank here
    multiple_keys = [str(customer + 1) for customer in max_keys]
    return multiple_keys


def report():
    for customer_id in range(len(overnight_reservations)):
        print(f"Customer {customer_id + 1} spent ${earning_per_customer(customer_id)}")
    print(f"Combined all customers paid ${total_earnings()} total")
    print(f"The total spent on baths was ${total_bath()}")
    print(f"${max(most_paid().values())} was the most paid by any single customer")
    print(f"The customer(s) that paid the most were: {','.join(most_spent_customers())}")
    
        
ada_doggy_getaway(overnight_reservations, bath_booked )