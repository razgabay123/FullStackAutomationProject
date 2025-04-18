import time

import allure
from selenium.webdriver.common.keys import Keys

from extensions.ui_actions import UiActions
import utilities.manage_pages as pages


class Desktop_Flows:
	@staticmethod
	@allure.step("write an equation for calculation. Eg; '1+1'")
	def calculate_flow(equ: str):
		for i in equ:
			Desktop_Flows.calculator_click(i)
		UiActions.click(pages.calculator.get_equal())
	
	@staticmethod
	def calculator_click(value):
		if value == '0':
			UiActions.click(pages.calculator.get_zero())
		elif value == '1':
			UiActions.click(pages.calculator.get_one())
		elif value == '2':
			UiActions.click(pages.calculator.get_two())
		elif value == '3':
			UiActions.click(pages.calculator.get_three())
		elif value == '4':
			UiActions.click(pages.calculator.get_four())
		elif value == '5':
			UiActions.click(pages.calculator.get_five())
		elif value == '6':
			UiActions.click(pages.calculator.get_six())
		elif value == '7':
			UiActions.click(pages.calculator.get_seven())
		elif value == '8':
			UiActions.click(pages.calculator.get_eight())
		elif value == '9':
			UiActions.click(pages.calculator.get_nine())
		elif value == '+':
			UiActions.click(pages.calculator.get_plus())
		elif value == '-':
			UiActions.click(pages.calculator.get_minus())
		elif value == '*':
			UiActions.click(pages.calculator.get_mult())
		elif value == '/':
			UiActions.click(pages.calculator.get_divide())
		else:
			raise Exception("Invalid Input" + value)
		
	@staticmethod
	def get_result_flow():
		result = pages.calculator.get_result().text.replace("Display is", " ").strip()
		return result
	
	@staticmethod
	@allure.step("clear the calculator")
	def clear_flow():
		UiActions.click(pages.calculator.get_clear())
		