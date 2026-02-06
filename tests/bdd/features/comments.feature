Feature: Comments API Testing
  As an API user
  I want to interact with comments endpoint
  So that I can manage comments data

  Scenario: Get all comments successfully
    Given the API is available
    When I send a GET request to "/comments"
    Then the response status code should be 200
    And the response should contain a list of comments

  Scenario: Filter comments by post ID
    Given the API is available
    When I send a GET request to "/comments" with query parameter
      | postId |
      | 1      |
    Then the response status code should be 200
    And all comments should belong to post 1

  Scenario: Create a new comment
    Given the API is available
    When I send a POST request to "/comments" with valid data
      | postId | name        | email           | body          |
      | 1      | Test User   | test@test.com   | Test comment  |
    Then the response status code should be 201
    And the response should contain the comment data
