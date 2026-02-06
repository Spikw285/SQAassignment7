Feature: Users API Testing
  As an API user
  I want to interact with users endpoint
  So that I can retrieve user information

  Scenario: Get all users successfully
    Given the API is available
    When I send a GET request to "/users"
    Then the response status code should be 200
    And the response should contain a list of users

  Scenario: Get a specific user by ID
    Given the API is available
    When I send a GET request to "/users/1"
    Then the response status code should be 200
    And the response should contain user details

  Scenario: Get user with invalid ID
    Given the API is available
    When I send a GET request to "/users/99999"
    Then the response status code should be 404
