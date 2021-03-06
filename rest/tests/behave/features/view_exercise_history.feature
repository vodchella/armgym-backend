Feature: View exercise history

  Scenario: Do it right
      Given I try to get exercise history right
       Then I will get Ok http status

  Scenario: Specify invalid ID
      Given I try to specify invalid exercise ID for view history
       Then I will get "400" http error with "-32001" application error

  Scenario: Specify nonexistent ID
      Given I try to specify nonexistent exercise ID for view history
       Then I will get "400" http error with "-32002" application error
