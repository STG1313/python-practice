import pytest
from rating_storage import ratings, save_rating


@pytest.fixture
def clean_ratings():
    ratings.clear()
    yield
    ratings.clear()


def test_save_rating(clean_ratings):
    result = save_rating(5)

    assert result == "Сохранено"
    assert ratings == [5]


def test_invalid_rating_is_not_saved(clean_ratings):
    result = save_rating(100)

    assert result == "Ошибка"
    assert ratings == []
