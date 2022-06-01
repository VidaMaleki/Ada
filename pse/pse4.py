#word = "Hello, world!"
word = "racecar"
# def palindrome(word):
#     if type(word) is not str:
#         raise TypeError("Input must be string")
#     if not word :
#         raise ValueError("Empty string")
    
#     reversed_word = word[::-1]
#     if word.lower() == reversed_word.lower():
#         return True
#     return False


def palindrome(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    return False

print(palindrome(word))