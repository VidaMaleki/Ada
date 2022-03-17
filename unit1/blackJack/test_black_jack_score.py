from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  # Act
  score = blackjack_score(hand)
  # Assert <-- Right assert statement here
  assert score == 7

#@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  # list = ["King", "Queen", "Jack"]
  # for i in list:
  #     score = blackjack_score(i)
  #     assert score == 10

  hand = ["King", 2]
  score = blackjack_score(hand)
  assert score == 12

  hand = ["Queen", 2]
  score = blackjack_score(hand)
  assert score == 12

  hand = ["Jack", 2]
  score = blackjack_score(hand)
  assert score == 12

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ["Ace", 5, 3]
  score = blackjack_score(hand)
  assert score == 19

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = ["Jack",2,"Ace"]
  score = blackjack_score(hand)
  assert score == 13

def test_calculates_21_with_ace_followed_by_jack():
  hand = ["Ace", "Jack"]
  score = blackjack_score(hand)
  assert score == 21

def test_calculates_21_with_2_aces_and_9():
  hand = ["Ace", 9, "Ace"]
  score = blackjack_score(hand)
  assert score == 21

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = ["abc"]
  score = blackjack_score(hand)
  assert score == "Invalid"

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, 3, 4, 5, 6, 7]
  score = blackjack_score(hand)
  assert score == "Invalid"

def test_returns_invalid_for_list_length_less_than_2():
  hand = [2]
  score = blackjack_score(hand)
  assert score == "Invalid"

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [2, 6, 7, 8]
  score = blackjack_score(hand)
  assert score == "Bust"