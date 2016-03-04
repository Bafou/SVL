import behave
from selenium import webdriver
import nose.tools

@given('I am on the calculator page')
def step_impl(context):
	context.navigateur.get('http://localhost:8080/')
    
@when('I enter a height value and validate')
def step_impl(context):
	input_box = context.navigateur.find_element_by_xpath("//input")
	input_box.send_keys("1.60")
	input_box.submit()

@then('I can see the ideal weight corresponding')
def step_impl(context):
	message = context.navigateur.find_element_by_id('id_resultat')
	text = message.text
	nose.tools.assert_true("57.5" in text)

@when('I enter a height value and tick the man radio button and validate')
def step_impl(context):
	input_box = context.navigateur.find_element_by_xpath("//input")
	input_box.send_keys("1.60")
	man_button = context.navigateur.find_element_by_xpath("//input[@id='id_bouton_homme']")
	man_button.click()
	input_box.submit()

@then('I can see the ideal weight corresponding for a man')
def step_impl(context):
	message = context.navigateur.find_element_by_id('id_resultat')
	text = message.text
	nose.tools.assert_true("57.5" in text)

@when('I enter a height value and tick the woman radio button and validate')
def step_impl(context):
	input_box = context.navigateur.find_element_by_xpath("//input")
	input_box.send_keys("1.60")
	man_button = context.navigateur.find_element_by_xpath("//input[@id='id_bouton_femme']")
	man_button.click()
	input_box.submit()

@then('I can see the ideal weight corresponding for a woman')
def step_impl(context):
	message = context.navigateur.find_element_by_id('id_resultat')
	text = message.text
	nose.tools.assert_true("56.0" in text)

@when('I enter a negative value')
def step_impl(context):
	input_box = context.navigateur.find_element_by_xpath("//input")
	input_box.send_keys("-1.50")
	input_box.submit()

@then('I can see an error message')
def step_impl(context):
	message = context.navigateur.find_element_by_id('id_message_valeur_erronee')
	text = message.text
	nose.tools.assert_true("Valeur erronée" in text)

@when('I enter a string value')
def step_impl(context):
	input_box = context.navigateur.find_element_by_xpath("//input")
	input_box.send_keys("cookies")
	input_box.submit()