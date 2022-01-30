SNOWMAN_WORD = "pasta"

def get_letter_from_user():
    letter = input("Please enter a letter > ")
    if len(letter) > 1 or not letter.isalpha():
        print("Invalid letter please enter a single character.")
    
    return letter


def snowman():
    # Your code is here
    get_letter = get_letter_from_user()
    if get_letter in SNOWMAN_WORD:
        print("Letter found")
    else:
        print("letter not found")
    if get_letter in SNOWMAN_WORD:
        return True
    else:
        return False

snowman()