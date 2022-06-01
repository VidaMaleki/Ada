def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Inavalid input: input must be greater than zero")
    return factorial(n -1) * n 

print(factorial(5)) #120

# def reverse(s):
    
#     if s == "":
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
    
#print(reverse("sepanta"))
# 
# 
# sepanta --> epanta + s = epantas
# epanta --> panta + p =  pantae
# panta --> anta + a = 
# anta --> nta + n
# nta --> ta + t
# ta --> a
# a

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" and parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])
        
        
print(is_nested_parens("()()))"))

s = str(18758368)
print()

