from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
gbp_input = (By.ID, 'etAmount')
years_input = (By.ID, 'etTerm')
percent_input = (By.ID, 'etRate')
calc_button = (By.ID, 'btnCalculate')
repayment_value = (By.ID, 'tvRepayment')
interest_value = (By.ID, 'tvInterestOnly')
save_button = (By.ID, 'btnSave')


class Calculator_Page:
	def __init__(self, driver) -> None:
		self.driver = driver
		
	def get_gbp(self) -> WebElement:
		return self.driver.find_element(gbp_input[0], gbp_input[1])
	
	def get_years(self) -> WebElement:
		return self.driver.find_element(years_input[0], years_input[1])
	
	def get_percentage(self) -> WebElement:
		return self.driver.find_element(percent_input[0], percent_input[1])
	
	def get_calc_button(self) -> WebElement:
		return self.driver.find_element(calc_button[0], calc_button[1])
	
	def get_repayment(self) -> WebElement:
		return self.driver.find_element(repayment_value[0], repayment_value[1])
	
	def get_interest(self) -> WebElement:
		return self.driver.find_element(interest_value[0], interest_value[1])
	
	def get_save_btn(self) -> WebElement:
		return self.driver.find_element(save_button[0], save_button[1])
# Last updated: 2025-11-26
