from selenium.webdriver.common.by import By

username = (By.ID, "username")
password = (By.ID, "password")
button = (By.ID, "submit")


class Login_Page():
	def __init__(self, driver):
		self.driver = driver
		
	def get_username_input(self):
		return self.driver.find_element(username[0], username[1])
	
	def get_password_input(self):
		return self.driver.find_element(password[0], password[1])
	
	def get_login_button(self):
		return self.driver.find_element(button[0], button[1])
	