Feature: Landing Page
    This feature implements the main landing page.

    @fixture.chrome.driver
    Scenario: Title present
        Given open homepage
        When homepage is opened 
        Then verify title is present