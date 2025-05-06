Feature: Authentication API Testing

  Scenario: Successful login with valid credentials
    #noinspection CucumberUndefinedStep
    Given I set the login payload with username "emilys" and password "emilyspass"
    #noinspection CucumberUndefinedStep
    When I send a POST request to the login endpoint
    #noinspection CucumberUndefinedStep
    Then the response should contain a token
    #noinspection CucumberUndefinedStep
    And the response status code should be 200

  Scenario: Login fails with invalid credentials
    #noinspection CucumberUndefinedStep
    Given I set the login payload with username "invalid_user" and password "wrong_pass"
    #noinspection CucumberUndefinedStep
    When I send a POST request to the login endpoint
    #noinspection CucumberUndefinedStep
    Then the response status code should be 400
    #noinspection CucumberUndefinedStep
    And the response should contain an error message

  Scenario: Access protected resource with valid token
    #noinspection CucumberUndefinedStep
    Given I am logged in with username "emilys" and password "emilyspass"
    #noinspection CucumberUndefinedStep
    When I access the protected resource "https://dummyjson.com/auth/me"
    #noinspection CucumberUndefinedStep
    Then the response should contain the username "emilys"
       #noinspection CucumberUndefinedStep
    And the response status code should be 200

  Scenario: Access protected resource with invalid token
    #noinspection CucumberUndefinedStep
    Given I use an invalid token "fake.jwt.token"
    #noinspection CucumberUndefinedStep
    When I access the protected resource "https://dummyjson.com/auth/me"
    #noinspection CucumberUndefinedStep
    Then the response status code should be 500
