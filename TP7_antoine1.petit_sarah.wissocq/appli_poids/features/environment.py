from selenium import webdriver

def before_all(context):
	context.navigateur = webdriver.Firefox()

def after_all(context):
	context.navigateur.quit()