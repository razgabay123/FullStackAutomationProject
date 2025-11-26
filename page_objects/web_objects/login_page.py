from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

username = (By.ID, "username")
password = (By.ID, "password")
button = (By.ID, "submit")


class Login_Page():
	def __init__(self, driver) -> None:
		self.driver = driver
		
	def get_username_input(self) -> WebElement:
		return self.driver.find_element(username[0], username[1])
	
	def get_password_input(self) -> WebElement:
		return self.driver.find_element(password[0], password[1])
	
	def get_login_button(self) -> WebElement:
		return self.driver.find_element(button[0], button[1])
# Last updated: 2025-11-26
