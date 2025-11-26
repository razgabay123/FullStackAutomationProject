import allure
from appium.webdriver import WebElement
from appium.webdriver.common.multi_action import MultiAction as multia
import test_cases.conftest as conf
from extensions.ui_actions import UiActions


class Touch_Actions(UiActions):
	@staticmethod
	@allure.step("tap a element")
	def tap_action(elem: WebElement, times: int) -> None:
		conf.action.tap(elem, times)
		
	@staticmethod
	@allure.step("Touch & hold a element")
	def touch_hold(elem: WebElement, wait: float) -> None:
		conf.action.long_press(elem, wait).perform()
		
	@staticmethod
	@allure.step("Swipe to a direction")
	def swipe_action(start_x: int, start_y: int, end_x: int, end_y: int, dur: int) -> None:
		conf.driver.swipe(start_x, start_y, end_x, end_y, dur)
	
	@staticmethod
	@allure.step("Zoom in")
	def zoom_action(x1: int, x2: int, y1: int, y2: int, wait: float) -> None:
		action1 = conf.action
		action2 = conf.action
		m_action = multia
		action1.long_press(x1, y1).move_to(x2, y2 + 90).wait(wait).release()
		action2.long_press(x1, y1).move_to(x2, y2 - 90).wait(wait).release()
		m_action.perform()
	
	@staticmethod
	@allure.step("Zoom out")
	def pinch(x1: int, x2: int, y1: int, y2: int, wait: float) -> None:
		action1 = conf.action
		action2 = conf.action
		m_action = multia
		action1.long_press(x1, y1 + 90).move_to(x2, y2).wait(wait).release()
		action2.long_press(x1, y1 - 90).move_to(x2, y2).wait(wait).release()
		m_action.perform()
# Last updated: 2025-11-26
