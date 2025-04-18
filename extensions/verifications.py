import allure
import pytest
import selenium.common.exceptions
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf
import utilities.common_ops as ops


class Verifications:
	@staticmethod
	@allure.step("Verify that something equals to another")
	def verify_equals(actual, expected):
		try:
			assert actual == expected
		except Exception as e:
			ops.attach_file(conf.driver)
			pytest.fail(f"Verification failed, '{actual}' doesnt equal to '{expected}'. " + str(e))
			
	@staticmethod
	@allure.step("Verify that a webelement is displayed")
	def is_displayed(elem: WebElement):
		try:
			assert elem.is_displayed(), f"Verification failed, element: '{elem.text}' isn't displayed."
		except Exception as e:
			ops.attach_file(conf.driver)
			pytest.fail(f"Verification failed, element: '{elem.text}' isn't displayed. " + str(e))
	
	@staticmethod
	@allure.step("Verify that a webelement is not displayed")
	def is_not_displayed(elem: WebElement):
		try:
			assert selenium.common.exceptions.NoSuchElementException(elem)
		except Exception as e:
			ops.attach_file(conf.driver)
			pytest.fail(f"Verification failed, element: '{elem.text}' exits. " + str(e))
