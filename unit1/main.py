VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    num_aces = 0

    for card in hand:
        if card not in VALID_CARDS or (len(hand) < 2) or (len(hand) > 5):
            return "Invalid"
        elif card == "Jack" or card == "Queen" or card == "King":
            score += 10
        elif card != "Ace":
            score += card
        elif card == "Ace":
            num_aces += 1

    for i in range(num_aces):
        if (21 - score) >= 11:
            score += 11
        else:
            score += 1

    if score > 21:
        return "Bust"
    return score