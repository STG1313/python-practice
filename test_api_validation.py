from api_validation import is_valid_product_response
import pytest




def test_valid_product_response():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is True


def test_empty_product_name():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "   ",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is False


def test_boolean_price_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": True
        }
    }

    assert is_valid_product_response(response) is False   


def test_wrong_status_code():
    response = {
        "status_code": 500,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is False



def test_nan_price_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": float("nan")
        }
    }    

    assert is_valid_product_response(response) is False


def test_infinite_price_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": float("inf")
        }
    }

    assert is_valid_product_response(response) is False


def test_negative_price_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": 42,
            "name": "Keyboard",
            "price": -100
        }
    }

    assert is_valid_product_response(response) is False

def test_missing_product_id():
    response = {
        "status_code": 200,
        "body": {
            "name": "Keyboard",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is False    

def test_boolean_product_id_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": True,
            "name": "Keyboard",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is False   


def test_response_is_not_dict():
    response = None

    assert is_valid_product_response(response) is False  


@pytest.mark.parametrize("body, expected", [
    (None, False),
    ("Keyboard", False),
    (["Keyboard", 2500], False),
])   

def test_invalid_body_types(body, expected):
    response = {
        "status_code": 200,
        "body": body
    }
    assert is_valid_product_response(response) is expected


def test_float_product_id_is_invalid():
    response = {
        "status_code": 200,
        "body": {
            "id": 42.5,
            "name": "Keyboard",
            "price": 2500
        }
    }

    assert is_valid_product_response(response) is False    
