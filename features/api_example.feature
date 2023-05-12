Feature: Test API
  Scenario: Test API
    Given I request a new widget for an account via SOAP
    Then I should receive an OK SOAP response

    