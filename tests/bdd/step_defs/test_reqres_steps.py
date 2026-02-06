import requests
from pytest_bdd import scenarios, given, when, then, parsers

# Load scenarios
scenarios('../features/reqres_users.feature')

BASE_URL = "https://reqres.in/api"

@given('the ReqRes API is available')
def reqres_api_available(context):
    """Verify ReqRes API is reachable"""
    response = requests.get(f"{BASE_URL}/users?page=1")
    assert response.status_code == 200

@when(parsers.parse('I send a GET request to ReqRes "{endpoint}" with page {page:d}'))
def send_get_reqres_paginated(context, endpoint, page):
    """Send GET request with pagination"""
    context['response'] = requests.get(f"{BASE_URL}{endpoint}?page={page}")

@when('I send a POST request to ReqRes "/users" with user data')
def send_post_reqres_user(context):
    """Send POST request to create user"""
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    context['response'] = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

@when('I send a POST request to ReqRes "/login" with credentials')
def send_post_login(context):
    """Send POST request for login"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    context['response'] = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

@when('I send a POST request to ReqRes "/login" with only email')
def send_post_login_no_password(context):
    """Send POST request with missing password"""
    payload = {
        "email": "eve.holt@reqres.in"
    }
    context['response'] = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

@then('the response should contain paginated user data')
def check_paginated_data(context):
    """Verify paginated response structure"""
    data = context['response'].json()
    assert 'data' in data
    assert 'page' in data
    assert 'per_page' in data
    assert 'total' in data
    assert isinstance(data['data'], list)

@then('the response should contain created user with timestamp')
def check_created_user(context):
    """Verify created user response"""
    data = context['response'].json()
    assert 'name' in data
    assert 'job' in data
    assert 'id' in data
    assert 'createdAt' in data

@then('the response should contain authentication token')
def check_auth_token(context):
    """Verify authentication token in response"""
    data = context['response'].json()
    assert 'token' in data
    assert isinstance(data['token'], str)
    assert len(data['token']) > 0

@then('the response should contain error message')
def check_error_message(context):
    """Verify error message in response"""
    data = context['response'].json()
    assert 'error' in data
