Feature: ReqRes Users API Testing
  As an API user
  I want to interact with ReqRes users endpoint
  So that I can manage user data

  Scenario: Get paginated users list
    Given the ReqRes API is available
    When I send a GET request to ReqRes "/users" with page 1
    Then the response status code should be 200
    And the response should contain paginated user data

  Scenario: Create a new user in ReqRes
    Given the ReqRes API is available
    When I send a POST request to ReqRes "/users" with user data
      | name      | job                |
      | John Doe  | Software Engineer  |
    Then the response status code should be 201
    And the response should contain created user with timestamp

  Scenario: Login with valid credentials
    Given the ReqRes API is available
    When I send a POST request to ReqRes "/login" with credentials
      | email               | password    |
      | eve.holt@reqres.in  | cityslicka  |
    Then the response status code should be 200
    And the response should contain authentication token

  Scenario: Login fails without password
    Given the ReqRes API is available
    When I send a POST request to ReqRes "/login" with only email
      | email               |
      | eve.holt@reqres.in  |
    Then the response status code should be 400
    And the response should contain error message
