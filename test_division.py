import pytest
from division import divide


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (12, 3, 4.0),
    (-12, 3, -4.0),
    (0, 5, 0.0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected
