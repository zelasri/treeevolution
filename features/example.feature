Feature: Search
    Scenario: Search PyPI
        Given I navigate to the PyPi Home page
        When I search for "behave"
        Then I find a link to project "behave"
        And If I click on project "behave", I find its version "1.2.6"