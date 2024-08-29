Feature: Verify the sale status
  Scenario:  User can filter by sale status "Announced"
    Given Open the main page
    When Log in to the page
    And Click on “off plan” at the left side menu
    And Verify the right page opens
    And Filter by sale status of “Announced”
    Then Verify each product contains the Announced tag

