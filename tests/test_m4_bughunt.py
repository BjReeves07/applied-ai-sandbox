from scratch import average_rating

def test_empty_ratings_returns_zero():
    assert average_rating([]) == 0.0

def test_normal_ratings():
    assert average_rating([4, 5, 3]) == 4.0
