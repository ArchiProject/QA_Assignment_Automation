import requests
from behave import given, when, then

BASE_URL = "https://dummyjson.com/auth"
context = {}

@given('I set the login payload with username "{username}" and password "{password}"')
def step_set_login_payload(context, username, password):
    print("Step matched and running!")
    context.payload = {
        "username": username,
        "password": password,
        "expiresInMins": 30  # Optional, defaults to 60
    }

@when('I send a POST request to the login endpoint')
def step_send_login_request(context):
    response = requests.post(f"{BASE_URL}/login", json=context.payload)
    context.response = response
    if response.status_code == 200:
        context.token = response.json().get("accessToken")

@then('the response status code should be {status_code:d}')
def step_check_status_code(context, status_code):
    # print("Payload being sent:", context.payload)
    # print("DEBUG - Actual status code:", context.response.status_code)
    # print("DEBUG - Expected status code:", status_code)
    # print("DEBUG - Response body:", context.response.text)
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

# @then('the response should contain a token')
# def step_check_token(context):
#     data = context.response.json()
#     print("Login response JSON:", data)
#     assert "accessToken" in data, "Access token not found in response"
@then('the response should contain a token')
def step_check_token(context):
    data = context.response.json()
    print("Login response JSON:", data)  # Optional: useful for debugging
    assert "accessToken" in data, "Access token not found in response"
    context.token = data["accessToken"]  # Store the token for later use

@given('I am logged in with username "{username}" and password "{password}"')
def step_login_and_store_token(context, username, password):
    payload = {
        "username": username,
        "password": password,
        "expiresInMins": 30
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200, "Login failed"
    # context.token = response.json().get("accessToken")
    context.token = response.json().get("accessToken")

@given('I use an invalid token "{token}"')
def step_set_invalid_token(context, token):
    context.token = token

@when('I access the protected resource "{url}"')
def step_access_protected_resource(context, url):
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.get(url, headers=headers)
    context.response = response

@then('the response should contain the username "{expected_username}"')
def step_check_username_in_response(context, expected_username):
    # print("Step matched and running!")
    # print("Payload being sent:", context.payload)
    data = context.response.json()
    assert data.get("username") == expected_username, \
        f"Expected username '{expected_username}', got '{data.get('username')}'"

@then('the response should contain an error message')
def step_check_error_message(context):
    data = context.response.json()
    print("Response JSON:", data)  # For debugging
    assert 'message' in data, "Error message not found in the response"
    error_message = data.get('message')
    print(f"Error message: {error_message}")