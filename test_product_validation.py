from product_validation import validate_product
import pytest


@pytest.mark.parametrize(
    "product, expected",
    [
        ({"name": "Phone", "price": 100}, True),
        ({"name": "", "price": 100}, False),
        ({"name": "  ", "price": 100}, False),
        ({"name": "Phone", "price": True}, False),
        ({"name": "Phone", "price": False}, False),
        ({"name": "Phone", "price": None}, False),
        ({"name": "Phone", "price": float("nan")}, False),
        ({"name": "Phone", "price": float("inf")}, False),
        ({"name": "Phone", "price": 0}, False),
    ],
)
def test_product_validate(product, expected):
    assert validate_product(product) is expected
