import pytest


@pytest.fixture
def ratings():
    return []


def test_add_rating(ratings):
    ratings.append(4)
    assert ratings == [4]


def test_empty_ratings(ratings):
    assert ratings == []
