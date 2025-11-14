from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

create = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.CLASS_NAME, "view_2Ow90")
delete_button = (By.XPATH, "//div[@class='view_2Ow90']/*[name()='svg']")


class TaskPage:
	def __init__(self, driver) -> None:
		self.driver = driver

	def get_create(self) -> List[WebElement]:
		return self.driver.find_elements(create[0], create[1])
		
	def get_tasks(self) -> List[WebElement]:
		return self.driver.find_elements(tasks[0], tasks[1])
	
	def get_deletes(self) -> List[WebElement]:
		return self.driver.find_elements(delete_button[0], delete_button[1])
	