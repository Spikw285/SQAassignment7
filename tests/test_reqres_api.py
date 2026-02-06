import requests
import pytest
import logging

logger = logging.getLogger(__name__)

class TestReqResAPI:
    BASE_URL = "https://reqres.in/api"
    
    # ========== POSITIVE SCENARIOS ==========
    
    @pytest.mark.positive
    @pytest.mark.reqres
    @pytest.mark.smoke
    def test_get_users_list_success(self):
        """Test 21: GET list of users - valid request"""
        logger.info("Testing GET list of users from ReqRes")
        
        endpoint = f"{self.BASE_URL}/users?page=1"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 200
        logger.info("✓ Status code is 200")
        
        data = response.json()
        assert 'data' in data
        assert isinstance(data['data'], list)
        logger.info(f"✓ Retrieved {len(data['data'])} users")
        
        assert len(data['data']) > 0
        logger.info("TEST PASSED: Successfully retrieved users list")
    
    @pytest.mark.positive
    @pytest.mark.reqres
    def test_get_single_user_success(self):
        """Test 22: GET single user by ID"""
        logger.info("Testing GET single user by ID")
        
        user_id = 2
        endpoint = f"{self.BASE_URL}/users/{user_id}"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 200
        data = response.json()
        assert 'data' in data
        assert data['data']['id'] == user_id
        
        logger.info(f"✓ Retrieved user with ID {user_id}: {data['data'].get('email')}")
        logger.info("TEST PASSED: Successfully retrieved single user")
    
    @pytest.mark.positive
    @pytest.mark.reqres
    def test_create_user_success(self):
        """Test 23: POST create new user"""
        logger.info("Testing POST create new user")
        
        payload = {
            "name": "John Doe",
            "job": "Software Engineer"
        }
        logger.debug(f"Request payload: {payload}")
        
        endpoint = f"{self.BASE_URL}/users"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 201
        logger.info("✓ Status code is 201 (Created)")
        
        data = response.json()
        assert data['name'] == payload['name']
        assert data['job'] == payload['job']
        assert 'id' in data
        assert 'createdAt' in data
        
        logger.info(f"✓ User created with ID: {data['id']}")
        logger.info(f"✓ Created at: {data['createdAt']}")
        logger.info("TEST PASSED: Successfully created new user")
    
    @pytest.mark.positive
    @pytest.mark.reqres
    def test_update_user_success(self):
        """Test 24: PUT update user"""
        logger.info("Testing PUT update user")
        
        payload = {
            "name": "Jane Doe",
            "job": "Team Lead"
        }
        logger.debug(f"Update payload: {payload}")
        
        endpoint = f"{self.BASE_URL}/users/2"
        response = requests.put(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        data = response.json()
        assert data['name'] == payload['name']
        assert 'updatedAt' in data
        
        logger.info(f"✓ User updated: {data['name']}")
        logger.info(f"✓ Updated at: {data['updatedAt']}")
        logger.info("TEST PASSED: Successfully updated user")
    
    @pytest.mark.positive
    @pytest.mark.reqres
    def test_login_success(self):
        """Test 25: POST login with valid credentials"""
        logger.info("Testing POST login with valid credentials")
        
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        logger.debug(f"Login with email: {payload['email']}")
        
        endpoint = f"{self.BASE_URL}/login"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        data = response.json()
        assert 'token' in data
        
        logger.info(f"✓ Login successful, token received: {data['token'][:10]}...")
        logger.info("TEST PASSED: Authentication successful")
    
    @pytest.mark.positive
    @pytest.mark.reqres
    def test_register_success(self):
        """Test 26: POST register new user"""
        logger.info("Testing POST register new user")
        
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        logger.debug(f"Registering with email: {payload['email']}")
        
        endpoint = f"{self.BASE_URL}/register"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        
        data = response.json()
        assert 'id' in data
        assert 'token' in data
        
        logger.info(f"✓ User registered with ID: {data['id']}")
        logger.info(f"✓ Token received: {data['token'][:10]}...")
        logger.info("TEST PASSED: Registration successful")
    
    # ========== NEGATIVE SCENARIOS ==========
    
    @pytest.mark.negative
    @pytest.mark.reqres
    def test_get_user_not_found(self):
        """Test 27: GET non-existent user"""
        logger.info("Testing GET non-existent user")
        
        endpoint = f"{self.BASE_URL}/users/999"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 404
        logger.info("✓ Correctly returned 404 for non-existent user")
        logger.info("TEST PASSED: Non-existent user handled correctly")
    
    @pytest.mark.negative
    @pytest.mark.reqres
    def test_login_missing_password(self):
        """Test 28: POST login without password"""
        logger.info("Testing POST login without password")
        
        payload = {"email": "eve.holt@reqres.in"}
        logger.debug(f"Login payload (missing password): {payload}")
        
        endpoint = f"{self.BASE_URL}/login"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 400
        
        data = response.json()
        assert 'error' in data
        
        logger.info(f"✓ Login rejected with error: {data['error']}")
        logger.info("TEST PASSED: Missing password validation works")
    
    @pytest.mark.negative
    @pytest.mark.reqres
    def test_register_missing_email(self):
        """Test 29: POST register without email"""
        logger.info("Testing POST register without email")
        
        payload = {"password": "pistol"}
        logger.debug(f"Register payload (missing email): {payload}")
        
        endpoint = f"{self.BASE_URL}/register"
        response = requests.post(endpoint, json=payload)
        
        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 400
        
        logger.info("✓ Registration rejected for missing email")
        logger.info("TEST PASSED: Missing email validation works")
    
    @pytest.mark.negative
    @pytest.mark.reqres
    def test_invalid_endpoint(self):
        """Test 30: Access invalid endpoint"""
        logger.info("Testing invalid endpoint")
        
        endpoint = f"{self.BASE_URL}/invalid"
        logger.debug(f"Sending GET request to: {endpoint}")
        
        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")
        
        assert response.status_code == 404
        logger.info("✓ Invalid endpoint returned 404")
        logger.info("TEST PASSED: Invalid endpoint handled correctly")
