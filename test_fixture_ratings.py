import pytest
from ratings import is_valid_rating


@pytest.fixture
def valid_ratings():
    return [1, 2, 3, 4, 5]

def test_all_ratings_are_valid(valid_ratings):
    for rating in valid_ratings:
        assert is_valid_rating(rating) is True 

def test_valid_ratings_count(valid_ratings):
    ratings = len(valid_ratings)
    assert ratings == 5
