# Python Practice

A collection of small Python projects created while learning Python programming and automated testing with pytest.

## Projects

### 1. Rating validation
Files: `ratings.py`, `test_ratings.py`, `test_fixture_ratings.py`

Validates integer ratings from 1 to 5. Tests cover valid values, invalid values, incorrect types, and pytest fixtures.

### 2. Rating storage
Files: `rating_storage.py`, `test_rating_storage.py`

Stores valid ratings in a list and rejects invalid ratings. Tests use a fixture to clean shared state before and after each test.

### 3. Division
Files: `division.py`, `test_division.py`

A simple division function. Tests cover positive, negative, and zero numerators, as well as division by zero.

### 4. Product API response validation
Files: `api_validation.py`, `test_api_validation.py`

Validates a sample product response object: status code, body type, product ID, product name, and price. Tests cover invalid types, missing fields, NaN, infinity, and invalid values.

This is validation of a sample response dictionary, not a live HTTP integration.

### 5. Product service
Files: `product_service.py`, `test_product_service.py`

Returns a product name when the response is valid and an error message when the response fails validation.

### 6. Pytest fixtures practice
File: `test_fixture_practice.py`

Demonstrates how pytest fixtures provide fresh test data for individual tests.

## Setup

Python 3.14 was used during development. Install the test dependency:

```bash
python -m pip install -r requirements.txt
```

Run all tests from the repository root:

```bash
python -m pytest -v
```

## Skills demonstrated

- Python functions and modules
- Input and response validation
- Type and value checking
- Positive, negative, and boundary test cases
- Parameterized tests
- pytest fixtures and cleanup
- Testing exceptions
- Basic service-layer logic
- Mutation-testing practice

This is a learning portfolio demonstrating foundational Python and automated testing practice.
