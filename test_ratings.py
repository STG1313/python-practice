import pytest
from ratings import is_valid_rating


@pytest.mark.parametrize("rating", [0, 6, -1, 100])
def test_invalid_ratings(rating):
    assert is_valid_rating(rating) is False


@pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
def test_valid_ratings(rating):
    assert is_valid_rating(rating) is True


@pytest.mark.parametrize("rating", [5.0, "5", True, None])
def test_invalid_types(rating):
    assert is_valid_rating(rating) is False 


@pytest.mark.parametrize(
    "rating, expected",
    [
        (1, True),
        (5, True),
        (0, False),
        (6, False),
    ]
)
def test_ratings(rating, expected):
    assert is_valid_rating(rating) is expected    
