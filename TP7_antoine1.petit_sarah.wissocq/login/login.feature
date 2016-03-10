Feature: Weight application 
	
	As an admin of the login application
	I want to create new login for an new user
	Because of reason.

	
	Scenario: the new login can't be the same as an older login
		Given I am on the calculator page
		When I enter a height value and validate
		Then I can see the ideal weight corresponding

		
	Scenario: the login is compose, at the most 8 first letters of the name
		Given I am on the calculator page
		When I enter a height value and validate
		Then I can see the ideal weight corresponding

	Scenario: if the login is already taken, the login must be the 7 first letters of the name (at the most) and the first letter of the last name.
		Given I am on the calculator page
		When I enter a height value and validate
		Then I can see the ideal weight corresponding
		
	Scenario: if there no other method, the admin choose a new login
		Given I am on the calculator page
		When I enter a height value and validate
		Then I can see the ideal weight corresponding
	
