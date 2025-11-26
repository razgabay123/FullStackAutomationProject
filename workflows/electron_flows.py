import time

import allure
from selenium.webdriver.common.keys import Keys

from extensions.ui_actions import UiActions
import utilities.manage_pages as pages


class Electron_Flows:
	@staticmethod
	@allure.step("Add a task")
	def create_task(task_description):
		UiActions.update_text(pages.todolist.get_create(), task_description)
		UiActions.update_text(pages.todolist.get_create(), Keys.RETURN)
		time.sleep(1.5)
		
	@staticmethod
	@allure.step("get the number of tasks")
	def get_number_of_tasks():
		return len(pages.todolist.get_tasks())
	
	@staticmethod
	@allure.step("Delete tasks")
	def delete_tasks():
		for x in range(Electron_Flows.get_number_of_tasks()):
			time.sleep(0.4)
			UiActions.mouse_hover_tooltip(pages.todolist.get_deletes()[0])
# Last updated: 2025-11-26
