import allure
import pytest

from extensions.verifications import Verifications
from workflows.electron_flows import Electron_Flows as flows


class Test_Electron:
	@allure.title("test01: create a task with a number")
	@allure.description("this test creates one task and verifies that the task been created")
	@pytest.mark.usefixtures('init_electron_driver')
	def test_01_create_a_new_task(self):
		flows.create_task("1")
		Verifications.verify_equals(flows.get_number_of_tasks(), 1)
		
	@allure.title("test02: Create 2 separate tasks")
	@allure.description("this test creates two more tasks and verifies that the tasks been created")
	def test_02_create_several_tasks(self):
		flows.create_task("Hello")
		flows.create_task("World")
		Verifications.verify_equals(flows.get_number_of_tasks(), 3)
	
	@allure.title("test03: Delete tasks")
	@allure.description("this test deletes all the tasks, and verifies that there are none")
	def test_03_delete_tasks(self):
		flows.delete_tasks()
		Verifications.verify_equals(flows.get_number_of_tasks(), 0)
# Last updated: 2025-11-26
