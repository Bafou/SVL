Feature: Login creation 
	
	As an admin of the login application
	I want to create new account for an new user giving his name, last name and login
	Because an account is needed in my application

	
		Scenario: the new login can't be the same as an older login
			Given I am on account creation page
			When I enter a name, last name, and login in creation form and the same login already exists
			Then I can see an error telling that an account already exist with this login
			
		Scenario: the account is created
			Given I am on account creation page
			When I enter a name, last name, and login in creation form and the login don't already exist in the database
			Then I can see that the account have been created

	As a administrator
	I want to create a new user in database only using his name and surname
	Because I want to the login creation to be automated
		
		Scenario: the login is compose, at the most 8 first letters of the name
			Given I am on account creation page
			When I enter enter a name, last name and the first strategy work
			Then I can see the account has been created and the login is composed at the most 8 first letters of the name

		Scenario: if the login is already taken, the login must be the 7 first letters of the name (at the most) and the first letter of the last name.
			Given I am on account creation page
			When  I enter enter a name, last name and the first strategy fail but the second work
			Then I can see the account has been created and the login is composed at the most of the 7 first letter of the name and the first letter of the last name
		
		Scenario: if there no other method, the admin choose a new login
			Given I am on account creation page
			When I enter enter a name, last name and the first and second strategy both failed
			Then  can see an error telling that neither strategies has worked
	

	
