# Python Practice

A collection of small Python projects created while learning Python programming and automated testing with pytest.

## Projects

### 1. Rating Validation

**Location:** `ratings/`

A small validation function that accepts integer ratings from 1 to 5 and rejects values outside that range or values of other types.

Run its tests:

```bash
python -m pytest -v ratings/test_ratings.py
```

### 2. Product API Response Validation

**Location:** `api-validation/`

A validator for a sample product API response. It checks:

- The response is a dictionary.
- The HTTP status code is 200.
- The response body is a dictionary.
- The product ID is a positive integer (booleans and floats are rejected).
- The product name is a non-empty string.
- The price is a positive finite integer or float (booleans, NaN, and infinity are rejected).

Run its tests:

```bash
python -m pytest -v api-validation/test_api_validation.py
```

## Setup

Python 3.14 was used during development. Install the test dependency:

```bash
python -m pip install -r requirements.txt
```

Run all tests from the repository root:

```bash
python -m pytest -v
```

## What this repository demonstrates

- Basic Python functions and conditional validation.
- Type and value checking.
- Positive and negative test cases.
- Parameterized tests with pytest.
- Testing invalid and boundary input values.
- A basic mutation-testing exercise: deliberately changing validation logic to check whether a test detects the defect.

## Learning status

This is a learning portfolio. The projects demonstrate foundational Python and automated testing practice; they are not production API integrations.
