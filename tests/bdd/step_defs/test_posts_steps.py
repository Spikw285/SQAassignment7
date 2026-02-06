import requests
from pytest_bdd import scenarios, given, when, then, parsers

# Load scenarios
scenarios('../features/posts.feature')

@given('the API is available')
def api_available(context):
    """Verify API is reachable"""
    response = requests.get(f"{context['base_url']}/posts")
    assert response.status_code == 200

@given('a post with ID 1 exists')
def post_exists(context):
    """Verify post exists"""
    response = requests.get(f"{context['base_url']}/posts/1")
    assert response.status_code == 200

@when(parsers.parse('I send a GET request to "{endpoint}"'))
def send_get_request(context, endpoint):
    """Send GET request"""
    context['response'] = requests.get(f"{context['base_url']}{endpoint}")

@when('I send a POST request to "/posts" with valid data')
def send_post_request(context):
    """Send POST request with data"""
    payload = {
        "title": "Test Post",
        "body": "Test post body",
        "userId": 1
    }
    context['response'] = requests.post(
        f"{context['base_url']}/posts",
        json=payload,
        headers=context['headers']
    )

@when('I send a PUT request to "/posts/1" with updated data')
def send_put_request(context):
    """Send PUT request to update post"""
    payload = {
        "id": 1,
        "title": "Updated Post",
        "body": "Updated body",
        "userId": 1
    }
    context['response'] = requests.put(
        f"{context['base_url']}/posts/1",
        json=payload,
        headers=context['headers']
    )

@when(parsers.parse('I send a DELETE request to "{endpoint}"'))
def send_delete_request(context, endpoint):
    """Send DELETE request"""
    context['response'] = requests.delete(f"{context['base_url']}{endpoint}")

@then(parsers.parse('the response status code should be {status_code:d}'))
def check_status_code(context, status_code):
    """Verify response status code"""
    assert context['response'].status_code == status_code

@then('the response should contain a list of posts')
def check_posts_list(context):
    """Verify response contains list of posts"""
    data = context['response'].json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'title' in data[0]

@then('the response should contain the post data')
def check_post_data(context):
    """Verify response contains post data"""
    data = context['response'].json()
    assert 'title' in data
    assert 'body' in data

@then('the post should be updated')
def check_post_updated(context):
    """Verify post was updated"""
    data = context['response'].json()
    assert data['title'] == "Updated Post"
