word = "hmomH"
def palindrome(word):
    if type(word) == int:
        raise TypeError("Input must be string")
    if not word :
        raise ValueError("Empty string")
    
    reversed_word = word[::-1]
    print(reversed_word)
    if word.lower() == reversed_word.lower():
        return True
    return False
    
print(palindrome(word))