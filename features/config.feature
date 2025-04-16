Feature: testing google
    Scenario: visit treevolution and check
        When we visit treevolution/config
        Then it should have a title "Configuration panel"
        When i looking for value for range type and comparing it
        When date of end of simulation  inferior of begin date
        Then Invalid start date and end date
        When enter valid start date and end date
        Then valid message
