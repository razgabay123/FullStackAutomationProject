
import allure
import pytest
import workflows.api_flows as flows


class Test_API:
	@allure.title("Test01: get all of page 1's employees")
	@allure.description("this test gets the data of all the employees from the server on page 1")
	def test_01_get_all_employees_from_page_1(self):
		flows.API_Flows.get_all_users(1, 200)
	
	@allure.title("Test02: get all of page 2's employees")
	@allure.description("this test gets the data of all the employees from the server on page 2")
	def test_02_get_users_page_2(self):
		flows.API_Flows.get_all_users(2, 200)
	
	@allure.title("Test03: get all of page 1 and 2's employees but shows only their data")
	@allure.description("this test gets the data of all the employees and excludes unrelevant data")
	def test_03_get_all_users_data_only(self):
		flows.API_Flows.get_all_users_data_only(1, 200)
		flows.API_Flows.get_all_users_data_only(2, 200)
		
	@allure.title("Test04: create an employee")
	@allure.description("this test creates a new user in the server, however the data doesnt really update")
	def test_04_create_user(self):
		flows.API_Flows.post_user({"name": "raz gabay", "job": "QA"}, 201)
		
	@allure.title("Test05: Update an employee")
	@allure.description("this test updates an employee by their ID, though the data doesnt really update")
	def test_05_update_user(self):
		# side note, this doesn't actually update anything, will still respond with code 200 however
		flows.API_Flows.update_user(5, {"first_name": "Raz", "last_name": "killer"}, 200)
		flows.API_Flows.get_user_by_id(5, 200)
	
	@allure.title("Test06: Get several employees by ids")
	@allure.description("this test gets employees data by their id, using data driven testing")
	@pytest.mark.parametrize("number", flows.id_data)
	def test_06_get_users_by_id(self, number):
		flows.API_Flows.get_user_by_id(number, 200)
		
	@allure.title("Test07: Delete employee")
	@allure.description("this test deletes an employee, though it doesn't really do so")
	def test_07_delete_user(self):
		flows.API_Flows.delete_user(1, 204)
		