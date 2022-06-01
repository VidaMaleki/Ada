num = 15

def fizz_buzz(num):
    new_list = []
    for index in range(1,num+1):
        if index % 3 == 0:
            new_list.append("Fizz")
        elif index % 5 == 0:
            new_list.append("Buzz")
        elif index % 15 == 0:
            new_list.append("FizzBuzz")
        else:
            new_list.append(str(index))
            
    return new_list

print(fizz_buzz(num))