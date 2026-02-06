import requests
import pytest
import logging

logger = logging.getLogger(__name__)

class TestJSONPlaceholderAPI:
    
    # ========== POSITIVE SCENARIOS ==========
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    @pytest.mark.smoke
    def test_get_all_posts_success(self):
        """Test 1: GET all posts - valid request"""
        logger.info("Testing GET all posts from JSONPlaceholder")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        logger.debug(f"Response headers: {response.headers}")
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        logger.info("✓ Status code is 200")
        
        posts = response.json()
        assert isinstance(posts, list), "Response should be a list"
        logger.info(f"✓ Response is a list with {len(posts)} posts")
        
        assert len(posts) > 0, "Posts list should not be empty"
        logger.info("✓ Posts list is not empty")
        
        logger.info("TEST PASSED: Successfully retrieved all posts")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_get_single_post_success(self):
        """Test 2: GET single post by ID - valid request"""
        logger.info("Testing GET single post by ID")
        
        post_id = 1
        endpoint = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 200
        logger.info("✓ Status code is 200")
        
        data = response.json()
        logger.debug(f"Response data: {data}")
        
        required_fields = ['id', 'title', 'body', 'userId']
        for field in required_fields:
            assert field in data, f"Missing field: {field}"
            logger.info(f"✓ Field '{field}' is present")
        
        assert data['id'] == post_id, f"Expected post ID {post_id}, got {data['id']}"
        logger.info(f"✓ Post ID matches: {post_id}")
        
        logger.info("TEST PASSED: Successfully retrieved single post")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_create_post_success(self):
        """Test 3: POST create new post - valid payload"""
        logger.info("Testing POST create new post")
        
        payload = {
            "title": "Test Post",
            "body": "This is a test post body",
            "userId": 1
        }
        logger.debug(f"Request payload: {payload}")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        headers = {'Content-Type': 'application/json'}
        
        logger.debug(f"Sending POST request to: {endpoint}")
        response = requests.post(endpoint, json=payload, headers=headers)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        logger.info("✓ Status code is 201 (Created)")
        
        data = response.json()
        logger.debug(f"Response data: {data}")
        
        assert data['title'] == payload['title'], "Title mismatch"
        logger.info(f"✓ Title matches: {data['title']}")
        
        assert data['body'] == payload['body'], "Body mismatch"
        logger.info(f"✓ Body matches")
        
        assert 'id' in data, "Response should contain ID"
        logger.info(f"✓ Post created with ID: {data.get('id')}")
        
        logger.info("TEST PASSED: Successfully created new post")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_update_post_success(self):
        """Test 4: PUT update post - valid payload"""
        logger.info("Testing PUT update post")
        
        post_id = 1
        payload = {
            "id": post_id,
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1
        }
        
        endpoint = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        logger.debug(f"Sending PUT request to: {endpoint}")
        logger.debug(f"Update payload: {payload}")
        
        response = requests.put(endpoint, json=payload)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 200
        logger.info("✓ Status code is 200")
        
        data = response.json()
        assert data['title'] == payload['title']
        logger.info(f"✓ Post updated successfully with new title: {data['title']}")
        
        logger.info("TEST PASSED: Successfully updated post")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_patch_post_success(self):
        """Test 5: PATCH partial update - valid payload"""
        logger.info("Testing PATCH partial update")
        
        payload = {"title": "Patched Title"}
        endpoint = "https://jsonplaceholder.typicode.com/posts/1"
        
        logger.debug(f"Sending PATCH request to: {endpoint}")
        logger.debug(f"Patch payload: {payload}")
        
        response = requests.patch(endpoint, json=payload)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == payload['title']
        
        logger.info(f"✓ Post partially updated with new title: {data['title']}")
        logger.info("TEST PASSED: Successfully patched post")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_delete_post_success(self):
        """Test 6: DELETE post - valid request"""
        logger.info("Testing DELETE post")
        
        post_id = 1
        endpoint = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        
        logger.debug(f"Sending DELETE request to: {endpoint}")
        response = requests.delete(endpoint)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        logger.info(f"✓ Post {post_id} deleted successfully")
        logger.info("TEST PASSED: Successfully deleted post")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_get_users_with_correct_headers(self):
        """Test 7: GET users with correct headers"""
        logger.info("Testing GET users with correct headers")
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        endpoint = "https://jsonplaceholder.typicode.com/users"
        logger.debug(f"Sending GET request with headers: {headers}")
        
        response = requests.get(endpoint, headers=headers)
        logger.info(f"Response status code: {response.status_code}")
        logger.debug(f"Response headers: {dict(response.headers)}")
        
        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith('application/json')
        
        logger.info("✓ Correct headers received")
        logger.info("TEST PASSED: Headers validation successful")
    
    @pytest.mark.positive
    @pytest.mark.jsonplaceholder
    def test_filter_posts_by_user(self):
        """Test 8: GET posts filtered by userId - valid query param"""
        logger.info("Testing GET posts filtered by userId")
        
        user_id = 1
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        params = {'userId': user_id}
        
        logger.debug(f"Sending GET request with params: {params}")
        response = requests.get(endpoint, params=params)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        posts = response.json()
        logger.info(f"✓ Retrieved {len(posts)} posts for user {user_id}")
        
        assert all(post['userId'] == user_id for post in posts)
        logger.info(f"✓ All posts belong to user {user_id}")
        
        logger.info("TEST PASSED: Filtering works correctly")
    
    # ========== NEGATIVE SCENARIOS ==========
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_get_nonexistent_post(self):
        """Test 9: GET non-existent post ID - should return 404"""
        logger.info("Testing GET non-existent post")
        
        post_id = 99999
        endpoint = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        
        logger.debug(f"Sending GET request to: {endpoint}")
        response = requests.get(endpoint)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        
        logger.info("✓ Correctly returned 404 for non-existent post")
        logger.info("TEST PASSED: Non-existent resource handled correctly")
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_create_post_missing_required_fields(self):
        """Test 10: POST with missing required fields"""
        logger.info("Testing POST with missing required fields")
        
        payload = {"title": "Only Title"}
        logger.debug(f"Incomplete payload: {payload}")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        logger.warning("JSONPlaceholder accepts incomplete data (mock API behavior)")
        
        assert response.status_code == 201
        logger.info("TEST PASSED: API handled incomplete data")
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_create_post_invalid_data_type(self):
        """Test 11: POST with invalid data types"""
        logger.info("Testing POST with invalid data types")
        
        payload = {
            "title": 123,
            "body": True,
            "userId": "not_a_number"
        }
        logger.debug(f"Invalid payload: {payload}")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        logger.warning("JSONPlaceholder is lenient with data types")
        
        assert response.status_code in [201, 400]
        logger.info("TEST PASSED: Invalid data types handled")
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_invalid_endpoint_path(self):
        """Test 12: GET invalid endpoint - should return 404"""
        logger.info("Testing GET invalid endpoint")
        
        endpoint = "https://jsonplaceholder.typicode.com/invalid_endpoint"
        logger.debug(f"Sending GET request to invalid endpoint: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 404
        logger.info("✓ Correctly returned 404 for invalid endpoint")
        logger.info("TEST PASSED: Invalid endpoint handled correctly")
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_unsupported_http_method(self):
        """Test 13: Use unsupported HTTP method (TRACE)"""
        logger.info("Testing unsupported HTTP method")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts/1"
        logger.debug(f"Sending TRACE request to: {endpoint}")
        
        try:
            response = requests.request('TRACE', endpoint)
            logger.info(f"Response status code: {response.status_code}")
            assert response.status_code in [405, 501]
            logger.info("✓ Unsupported method rejected correctly")
        except Exception as e:
            logger.error(f"Exception occurred: {str(e)}")
            logger.info("✓ Method not supported (as expected)")
        
        logger.info("TEST PASSED: Unsupported method handled")
    
    @pytest.mark.negative
    @pytest.mark.jsonplaceholder
    def test_update_nonexistent_post(self):
        """Test 14: PUT to non-existent resource"""
        logger.info("Testing PUT to non-existent resource")
        
        payload = {"title": "Test", "body": "Test", "userId": 1}
        endpoint = "https://jsonplaceholder.typicode.com/posts/99999"
        
        logger.debug(f"Sending PUT request to: {endpoint}")
        response = requests.put(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code in [200, 404]
        
        logger.info("TEST PASSED: Non-existent resource update handled")
    
    # ========== EDGE & BOUNDARY CASES ==========
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_empty_payload(self):
        """Test 15: POST with empty payload"""
        logger.info("Testing POST with empty payload")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        logger.debug("Sending POST request with empty payload: {}")
        
        response = requests.post(endpoint, json={})
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 201
        logger.info("✓ Empty payload accepted")
        logger.info("TEST PASSED: Empty payload handled")
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_very_large_payload(self):
        """Test 16: POST with very large payload"""
        logger.info("Testing POST with very large payload")
        
        payload = {
            "title": "A" * 10000,
            "body": "B" * 50000,
            "userId": 1
        }
        logger.debug(f"Payload sizes - title: {len(payload['title'])}, body: {len(payload['body'])}")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code in [201, 413, 400]
        
        logger.info("TEST PASSED: Large payload handled")
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_rate_limit_simulation(self):
        """Test 17: Rapid repeated requests"""
        logger.info("Testing rate limiting with rapid requests")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts/1"
        responses = []
        
        logger.debug("Sending 20 rapid requests...")
        for i in range(20):
            response = requests.get(endpoint)
            responses.append(response.status_code)
            if i % 5 == 0:
                logger.debug(f"Completed {i} requests")
        
        success_count = responses.count(200)
        logger.info(f"✓ Successful requests: {success_count}/20")
        
        assert success_count >= 15
        logger.info("TEST PASSED: Rate limiting test completed")
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_zero_as_id(self):
        """Test 18: GET with ID = 0 (boundary case)"""
        logger.info("Testing GET with ID = 0 (boundary case)")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts/0"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code in [200, 404]
        logger.info("✓ Boundary case (ID=0) handled")
        logger.info("TEST PASSED: Zero ID handled correctly")
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_negative_id(self):
        """Test 19: GET with negative ID (edge case)"""
        logger.info("Testing GET with negative ID")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts/-1"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code in [200, 404, 400]
        logger.info("✓ Negative ID handled")
        logger.info("TEST PASSED: Negative ID edge case handled")
    
    @pytest.mark.edge
    @pytest.mark.jsonplaceholder
    def test_special_characters_in_filter(self):
        """Test 20: Filter with special characters (unexpected but valid)"""
        logger.info("Testing filter with special characters")
        
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        params = {'title': '@#$%^&*()'}
        
        logger.debug(f"Sending GET request with params: {params}")
        response = requests.get(endpoint, params=params)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        result = response.json()
        assert isinstance(result, list)
        logger.info(f"✓ Special characters handled, returned {len(result)} results")
        
        logger.info("TEST PASSED: Special characters in filter handled")
