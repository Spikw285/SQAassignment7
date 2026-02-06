import requests
import pytest
import logging

logger = logging.getLogger(__name__)


class TestDummyAPI:
    BASE_URL = "https://dummyapi.io/data/v1"
    HEADERS = {
        'app-id': '6582a7c8d16c6b164f8e2e7e'  # Public test app-id
    }

    # ========== POSITIVE SCENARIOS ==========

    @pytest.mark.positive
    @pytest.mark.dummyapi
    @pytest.mark.smoke
    def test_get_users_list_success(self):
        """Test 31: GET list of users - valid request"""
        logger.info("Testing GET list of users from DummyAPI")

        endpoint = f"{self.BASE_URL}/user"
        logger.debug(f"Sending GET request to: {endpoint}")

        response = requests.get(endpoint, headers=self.HEADERS)
        logger.info(f"Response status code: {response.status_code}")

        assert response.status_code == 200
        logger.info("✓ Status code is 200")

        data = response.json()
        assert 'data' in data
        assert isinstance(data['data'], list)
        logger.info(f"✓ Retrieved {len(data['data'])} users")

        logger.info("TEST PASSED: Successfully retrieved users list")

    @pytest.mark.positive
    @pytest.mark.dummyapi
    def test_get_single_user_success(self):
        """Test 32: GET single user by ID"""
        logger.info("Testing GET single user by ID")

        # First get a user ID
        response = requests.get(f"{self.BASE_URL}/user", headers=self.HEADERS)
        user_id = response.json()['data'][0]['id']

        endpoint = f"{self.BASE_URL}/user/{user_id}"
        logger.debug(f"Sending GET request to: {endpoint}")

        response = requests.get(endpoint, headers=self.HEADERS)
        logger.info(f"Response status code: {response.status_code}")

        assert response.status_code == 200
        data = response.json()
        assert 'id' in data
        assert 'firstName' in data

        logger.info(f"✓ Retrieved user: {data.get('firstName')} {data.get('lastName')}")
        logger.info("TEST PASSED: Successfully retrieved single user")

    @pytest.mark.positive
    @pytest.mark.dummyapi
    def test_create_user_success(self):
        """Test 33: POST create new user"""
        logger.info("Testing POST create new user")

        payload = {
            "firstName": "Test",
            "lastName": "User",
            "email": f"test{pytest.__version__}@test.com"
        }
        logger.debug(f"Request payload: {payload}")

        endpoint = f"{self.BASE_URL}/user/create"
        response = requests.post(endpoint, json=payload, headers=self.HEADERS)

        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200

        data = response.json()
        assert data['firstName'] == payload['firstName']
        assert data['lastName'] == payload['lastName']

        logger.info(f"✓ User created with ID: {data['id']}")
        logger.info("TEST PASSED: Successfully created new user")

    # ========== NEGATIVE SCENARIOS ==========

    @pytest.mark.negative
    @pytest.mark.dummyapi
    def test_get_user_without_app_id(self):
        """Test 34: GET without app-id header - should return 403"""
        logger.info("Testing GET without app-id header")

        endpoint = f"{self.BASE_URL}/user"
        logger.debug(f"Sending GET request without app-id to: {endpoint}")

        response = requests.get(endpoint)
        logger.info(f"Response status code: {response.status_code}")

        assert response.status_code == 403
        logger.info("✓ Correctly returned 403 for missing app-id")
        logger.info("TEST PASSED: Missing authentication handled")

    @pytest.mark.negative
    @pytest.mark.dummyapi
    def test_get_nonexistent_user(self):
        """Test 35: GET non-existent user"""
        logger.info("Testing GET non-existent user")

        endpoint = f"{self.BASE_URL}/user/invaliduserid123"
        logger.debug(f"Sending GET request to: {endpoint}")

        response = requests.get(endpoint, headers=self.HEADERS)
        logger.info(f"Response status code: {response.status_code}")

        assert response.status_code in [400, 404]
        logger.info("✓ Non-existent user handled correctly")
        logger.info("TEST PASSED: Invalid user ID handled")

    @pytest.mark.negative
    @pytest.mark.dummyapi
    def test_create_user_missing_required_fields(self):
        """Test 36: POST with missing required fields"""
        logger.info("Testing POST with missing required fields")

        payload = {"firstName": "OnlyFirstName"}
        logger.debug(f"Incomplete payload: {payload}")

        endpoint = f"{self.BASE_URL}/user/create"
        response = requests.post(endpoint, json=payload, headers=self.HEADERS)

        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 400

        logger.info("✓ Missing fields validation works")
        logger.info("TEST PASSED: Validation working correctly")

    @pytest.mark.negative
    @pytest.mark.dummyapi
    def test_create_user_invalid_email(self):
        """Test 37: POST with invalid email format"""
        logger.info("Testing POST with invalid email")

        payload = {
            "firstName": "Test",
            "lastName": "User",
            "email": "notanemail"
        }
        logger.debug(f"Payload with invalid email: {payload}")

        endpoint = f"{self.BASE_URL}/user/create"
        response = requests.post(endpoint, json=payload, headers=self.HEADERS)

        logger.info(f"Response status code: {response.status_code}")
        assert response.status_code == 400

        logger.info("✓ Email validation works")
        logger.info("TEST PASSED: Invalid email rejected")