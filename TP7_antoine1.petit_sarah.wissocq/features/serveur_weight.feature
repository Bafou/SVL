Feature: Weight application 
	
	As a user(man or woman) of the weight application
	I want to calculate my ideal weight giving my height
	Because I want to be healthy.

	Scenario: the value is correctly displayed
		Given I am on the calculator page
		When I enter a height value and validate
		Then I can see the ideal weight corresponding

	Scenario: the value is correctly displayed for a man
		Given I am on the calculator page
		When I enter a height value and tick the man radio button and validate
		Then I can see the ideal weight corresponding for a man

	Scenario: the value is correctly displayed for a woman
		Given I am on the calculator page
		When I enter a height value and tick the woman radio button and validate
		Then I can see the ideal weight corresponding for a woman

	Scenario: the calculator refuses if the data is negative
		Given I am on the calculator page
		When I enter a negative value 
		Then I can see an error message

	Scenario: the calculator refuses if the data is a string
		Given I am on the calculator page
		When I enter a string value 
		Then I can see an error message