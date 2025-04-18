from selenium.webdriver.common.by import By
rate = (By.ID, 'tvRate')
delete_button = (By.ID, 'btnDel')
okay_button = (By.ID, 'button1')


class Saved_Calculations_Page:
	def __init__(self, driver):
		self.driver = driver
	
	def get_rate(self):
		return self.driver.find_element(rate[0], rate[1])
		
	def get_delete(self):
		return self.driver.find_element(delete_button[0], delete_button[1])
	
	def get_okay(self):
		return self.driver.find_element(okay_button[0], okay_button[1])
	