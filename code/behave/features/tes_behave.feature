@dev @APItest
Feature: TestAPIClass

  Scenario: testing for double number function in API class
    Given Randomly generate a source number and set into global variable
    When Call a double method and store the result in 1 seconds
    Then Check the double method results is correct or not

  Scenario: testing for plus one number function in API class
    Given Randomly generate a source number and set into global variable
    When Call a plus one method and store the result in 1 seconds
    Then Check the plus one results is correct or not