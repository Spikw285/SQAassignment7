Feature: Posts API Testing
  As an API user
  I want to interact with posts endpoint
  So that I can manage posts data

  Scenario: Get all posts successfully
    Given the API is available
    When I send a GET request to "/posts"
    Then the response status code should be 200
    And the response should contain a list of posts

  Scenario: Create a new post successfully
    Given the API is available
    When I send a POST request to "/posts" with valid data
      | title          | body                | userId |
      | Test Post      | Test post body      | 1      |
    Then the response status code should be 201
    And the response should contain the post data

  Scenario: Update a post successfully
    Given the API is available
    And a post with ID 1 exists
    When I send a PUT request to "/posts/1" with updated data
      | title          | body                | userId |
      | Updated Post   | Updated body        | 1      |
    Then the response status code should be 200
    And the post should be updated

  Scenario: Delete a post successfully
    Given the API is available
    When I send a DELETE request to "/posts/1"
    Then the response status code should be 200

  Scenario: Get non-existent post returns 404
    Given the API is available
    When I send a GET request to "/posts/99999"
    Then the response status code should be 404
