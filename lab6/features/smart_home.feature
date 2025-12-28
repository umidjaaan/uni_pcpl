Feature: Smart Home Control
  As a user
  I want to control my devices
  So that I can manage my home environment

  Scenario: Turning on a smart light
    Given a smart light is installed
    And the light is currently off
    When I turn the light on
    Then the light status should be "ON"
    And the system should return "Light is turned ON"
