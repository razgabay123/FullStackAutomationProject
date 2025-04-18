import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest as conf


# UI actions like clicking, hovering,etc
class UiActions:
	@staticmethod
	@allure.step("Click on an element")
	def click(elem: WebElement):
		elem.click()
		
	@staticmethod
	@allure.step("Input text")
	def update_text(elem: WebElement, value: str):
		elem.send_keys(value)
	
	@staticmethod
	@allure.step("Hover over 2 elements")
	def mouse_hover(elem1: WebElement, elem2: WebElement):
		conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()
	
	@staticmethod
	@allure.step("Right click on an element")
	def right_click(elem: WebElement):
		conf.action.context_click(elem).perform
		
	@staticmethod
	@allure.step('mouse hover tooltip (specifically made for electron)')
	def mouse_hover_tooltip(elem: WebElement):
		ActionChains(conf.driver).move_to_element(elem).click().perform()
	
	@staticmethod
	@allure.step("Drag an element from a to b")
	def drag_drop(elem1: WebElement, elem2: WebElement):
		conf.action.Drag_and_drop(elem1, elem2).perform()
	
	@staticmethod
	@allure.step("Clear input")
	def clear(elem: WebElement):
		elem.clear()
	
	@staticmethod
	@allure.step("Step back to a certain URL")
	def back_main(url):
		conf.driver.get(url)
		