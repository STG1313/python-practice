import pytest

from ratings import is_valid_rating


@pytest.mark.parametrize(
    "rating, expected",
    [
        (1, True),
        (5, True),
        (0, False),
        (6, False),
    ],
)
def test_is_valid_rating(rating, expected):
    assert is_valid_rating(rating) is expected
