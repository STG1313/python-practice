from api_validation import is_valid_product_response


def get_product_name(response):
    if not is_valid_product_response(response):
        return "Ошибка API"

    return response["body"]["name"]
