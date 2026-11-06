import math


def validate_product(product):
    if not isinstance(product, dict):
        return False

    name = product.get("name")
    price = product.get("price")

    if not isinstance(name, str) or not name.strip():
        return False

    if type(price) not in (int, float):
        return False

    if not math.isfinite(price):
        return False

    if price <= 0:
        return False

    return True
