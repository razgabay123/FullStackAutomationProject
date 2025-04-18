import pytest
from extensions.ui_actions import UiActions
import utilities.manage_pages as pages
from extensions.verifications import Verifications
import utilities.common_ops as ops
from page_objects.web_objects.page_transitioned_to import hero_title
from test_cases import conftest


class Web_Flows:
	# choose - functions for clicking each hero's input page
	@staticmethod
	def choose_iron_man():
		UiActions.click(pages.web_main.get_ironman())
	
	@staticmethod
	def choose_captain_america():
		UiActions.click(pages.web_main.get_captain_america())
	
	@staticmethod
	def choose_hulk():
		UiActions.click(pages.web_main.get_hulk())
	
	@staticmethod
	def choose_thor():
		UiActions.click(pages.web_main.get_thor())
		
	# chooses the hero to click + input based on hero's name in data
	@staticmethod
	def choose_hero(hero):
		if hero == 'ironman':
			Web_Flows.choose_iron_man()
		elif hero == 'captainamerica':
			Web_Flows.choose_captain_america()
		elif hero == 'hulk':
			Web_Flows.choose_hulk()
		elif hero == 'thor':
			Web_Flows.choose_thor()
			# fails if hero isn't recognised, removed, etc
		else:
			pytest.fail(f'that hero cannot be found: {hero}')
		
	# function for inputing user + pass
	@staticmethod
	def input_login(username: str, password: str):
		UiActions.update_text(pages.web_login.get_username_input(), username)
		UiActions.update_text(pages.web_login.get_password_input(), password)
		UiActions.click(pages.web_login.get_login_button())
	
	# function for verifying the hero name title, eg: ironman
	@staticmethod
	def verify_hero_title(expected: str):
		ops.wait(conftest.driver, ops.For.ELEMENT_DISPLAYED, hero_title)
		actual = pages.web_transition.get_hero_title().text
		Verifications.verify_equals(actual, expected)
	
	# function to go back to the main page at the start
	@staticmethod
	def go_back_main():
		UiActions.back_main(ops.get_data('URL'))


# data extraction from csv
logindata = ops.read_csv(ops.get_data('login-csv'))
login_data = [
			(logindata[0][0], logindata[0][1], logindata[0][2], logindata[0][3]),
			(logindata[1][0], logindata[1][1], logindata[1][2], logindata[1][3]),
			(logindata[2][0], logindata[2][1], logindata[2][2], logindata[2][3]),
			(logindata[3][0], logindata[3][1], logindata[3][2], logindata[3][3])
			]

