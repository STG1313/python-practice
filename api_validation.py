import math


def is_valid_product_response(response):
    if not isinstance(response, dict):
        return False

    if response.get("status_code") != 200:
        return False

    body = response.get("body")

    if not isinstance(body, dict):
        return False

    product_id = body.get("id")
    if type(product_id) is not int or product_id <= 0:
        return False

    name = body.get("name")
    if not isinstance(name, str) or not name.strip():
        return False

    price = body.get("price")
    if type(price) not in (int, float) or not math.isfinite(price) or price <= 0:
        return False

    return True
