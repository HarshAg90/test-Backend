
# Project Map

## Application

The main feature implementation is located in:

- `app.py` — Flask backend and API implementation
- `requirements.txt` — Python dependencies

## Tests

Tests are located in:

- `tests/test_app.py` — Test cases and assertions
- `tests/test_inputs.py` — Input values used by test cases

## Test Inputs

`tests/test_inputs.py` contains the concrete input payloads used
by the automated tests.

Important inputs include:

- `CREATE_USER_VALID_INPUT`
- `CREATE_USER_MISSING_NAME`
- `CREATE_USER_MISSING_EMAIL`
- `CREATE_USER_MISSING_PLAN`

## Feature Implementation

The primary implementation for user creation is:

- `app.py`
- Endpoint: `/api/create-user`

## CI/CD

CI configuration:

- `.github/workflows/ci.yml`

The CI workflow executes the automated tests in `tests/`.
