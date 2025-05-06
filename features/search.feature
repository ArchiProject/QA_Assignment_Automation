Feature: Search Functionality on SDAIA website

  As a user of the SDAIA website,
  I want to search for information using the search bar,
  So that I can find relevant content quickly.

  # ---------- VALID TESTS ----------
  Scenario: Valid search for a known term
    #noinspection CucumberUndefinedStep
    When I search for "AI"
    #noinspection CucumberUndefinedStep
    Then I should see relevant results for "AI"

  Scenario: Valid search using Arabic text
    #noinspection CucumberUndefinedStep
    When I search for "الذكاء الاصطناعي"
    #noinspection CucumberUndefinedStep
    Then I should see relevant results for "الذكاء الاصطناعي"

  # ---------- INVALID TESTS ----------
  Scenario: Submit an empty search
    #noinspection CucumberUndefinedStep
    When I search with an empty string
    #noinspection CucumberUndefinedStep
    Then I should be prompted to enter a search term

  Scenario: Search using only special characters
    #noinspection CucumberUndefinedStep
    When I search for "@#$%"
    #noinspection CucumberUndefinedStep
    Then I should see a message indicating no results were found

  # ---------- EDGE CASES ----------
  Scenario: Search with leading and trailing spaces
    #noinspection CucumberUndefinedStep
    When I search for "   Vision 2030   "
    #noinspection CucumberUndefinedStep
    Then I should see relevant results for "Vision 2030"

  Scenario: Search using a script tag (XSS attempt)
    #noinspection CucumberUndefinedStep
    When I search for "<script>alert('XSS')</script>"
    #noinspection CucumberUndefinedStep
    Then I should see a message indicating no results were found
    #noinspection CucumberUndefinedStep
    And the input should be sanitized
