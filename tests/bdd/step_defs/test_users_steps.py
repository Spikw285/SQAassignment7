import requests
from pytest_bdd import scenarios, when, then

# Load scenarios
scenarios('../features/users.feature')

@then('the response should contain a list of users')
def check_users_list(context):
    """Verify response contains list of users"""
    data = context['response'].json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'email' in data[0]

@then('the response should contain user details')
def check_user_details(context):
    """Verify response contains user details"""
    data = context['response'].json()
    assert 'id' in data
    assert 'name' in data
    assert 'email' in data
    assert 'address' in data
