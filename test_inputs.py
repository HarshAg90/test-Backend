# test_inputs.py

CREATE_USER_VALID_INPUT = {
    "name": "Harsh",
    "email": "harsh@example.com",
    "plan": "pro"
}

CREATE_USER_MISSING_NAME = {
    "email": "harsh@example.com",
    "plan": "pro"
}

CREATE_USER_MISSING_EMAIL = {
    "name": "Harsh",
    "plan": "pro"
}

CREATE_USER_MISSING_PLAN = {
    "name": "Harsh",
    "email": "harsh@example.com"
}