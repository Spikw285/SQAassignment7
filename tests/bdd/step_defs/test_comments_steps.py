import requests
from pytest_bdd import scenarios, when, then

# Load scenarios
scenarios('../features/comments.feature')

@when('I send a GET request to "/comments" with query parameter')
def send_get_with_params(context):
    """Send GET request with query parameters"""
    context['response'] = requests.get(
        f"{context['base_url']}/comments",
        params={'postId': 1}
    )

@when('I send a POST request to "/comments" with valid data')
def send_post_comment(context):
    """Send POST request to create comment"""
    payload = {
        "postId": 1,
        "name": "Test User",
        "email": "test@test.com",
        "body": "Test comment"
    }
    context['response'] = requests.post(
        f"{context['base_url']}/comments",
        json=payload,
        headers=context['headers']
    )

@then('the response should contain a list of comments')
def check_comments_list(context):
    """Verify response contains list of comments"""
    data = context['response'].json()
    assert isinstance(data, list)
    assert len(data) > 0

@then('all comments should belong to post 1')
def check_comments_belong_to_post(context):
    """Verify all comments belong to specific post"""
    data = context['response'].json()
    assert all(comment['postId'] == 1 for comment in data)

@then('the response should contain the comment data')
def check_comment_data(context):
    """Verify response contains comment data"""
    data = context['response'].json()
    assert 'postId' in data
    assert 'name' in data
    assert 'email' in data
    assert 'body' in data
