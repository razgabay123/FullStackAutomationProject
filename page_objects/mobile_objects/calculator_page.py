from selenium.webdriver.common.by import By

gbp_input = (By.ID, 'etAmount')
years_input = (By.ID, 'etTerm')
percent_input = (By.ID, 'etRate')
calc_button = (By.ID, 'btnCalculate')
repayment_value = (By.ID, 'tvRepayment')
interest_value = (By.ID, 'tvInterestOnly')
save_button = (By.ID, 'btnSave')


class Calculator_Page:
	def __init__(self, driver):
		self.driver = driver
		
	def get_gbp(self):
		return self.driver.find_element(gbp_input[0], gbp_input[1])
	
	def get_years(self):
		return self.driver.find_element(years_input[0], years_input[1])
	
	def get_percentage(self):
		return self.driver.find_element(percent_input[0], percent_input[1])
	
	def get_calc_button(self):
		return self.driver.find_element(calc_button[0], calc_button[1])
	
	def get_repayment(self):
		return self.driver.find_element(repayment_value[0], repayment_value[1])
	
	def get_interest(self):
		return self.driver.find_element(interest_value[0], interest_value[1])
	
	def get_save_btn(self):
		return self.driver.find_element(save_button[0], save_button[1])
	