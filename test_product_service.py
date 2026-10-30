from product_service import get_product_name 


def test_get_product_name():
    response = {
        "status_code": 200,
        "body": {
        "id": 42,
        "name": "Keyboard",
        "price": 2500
        }
    }

    assert get_product_name(response) == "Keyboard"

def test_get_product_name_with_error_response():
    response = {
        "status_code": 404,
                "body": {}
    }  

    assert get_product_name(response) == "Ошибка API"

def test_get_product_name_with_invalid_body():
    response = {
        "status_code": 404,
        "body": {
        "id": 42,
        "price": 2500
        }
    }

    assert get_product_name(response) == "Ошибка API"    
