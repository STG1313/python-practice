# Python Practice

A collection of small Python projects created while learning Python programming and automated testing with pytest.

## 1. Rating validation

Files: `ratings.py`, `test_ratings.py`

A function that accepts integer ratings from 1 to 5 and rejects values outside that range or values of other types.

## 2. Product API response validation

Files: `api_validation.py`, `test_api_validation.py`

A validator for a sample product API response. It checks the response type and status code, body structure, positive integer product ID, non-empty product name, and positive finite numeric price. Booleans, NaN, infinity, invalid body types, and float IDs are rejected.

This is validation of a sample response object, not a live HTTP/API integration.

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

- Python functions and conditional validation
- Type and value checking
- Positive, negative, and boundary test cases
- Parameterized tests with pytest
- Mutation-testing practice: deliberately changing validation logic to check whether a test detects the defect

This is a learning portfolio demonstrating foundational Python and automated testing practice.
