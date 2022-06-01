
# Imagine programming the logic for a word game.

# In this game, every player submits one word. Each word gets a score based on the letters in the word and its point value.

# Create a function named score that is responsible for scoring a given word.

# This function should take in a string named word as a parameter. This function should return the word's total number of points.

# Refer to this table for the point values of each letter.


score_dict = {
    'A': 1, 'E': 1, 'I': 1, 'O':1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F':4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
# def score(word):
#     sum_scores = 0
#     word = word.upper()
#     for letter in word:
#         if letter not in score_dict:
#             score_dict[letter] = 0
#         sum_scores += score_dict[letter]
#     return sum_scores

def score(word):
    scores = 0
    for letter in word:
        scores += score_dict[letter]
    return scores

print(score("DOG"))

#tests
def test_case_for_total_score():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "DOG"
    # act
    # assert
    assert score(word) == 5

def test_insensitive_case():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "Dog"
    # act
    # assert
    assert score(word) == 5