import json

import allure

import utilities.common_ops as ops
from extensions.api_actions import API_Actions as action
from extensions.verifications import Verifications


class API_Flows:
	@staticmethod
	@allure.step("get all users")
	def get_all_users(data, expected_status):
		response = action.get(ops.Api_Data.page(data))
		status = response.status_code
		print(json.dumps(response.json(), indent=2), "\n")
		Verifications.verify_equals(status, expected_status)
		
	@staticmethod
	@allure.step("get all users, prints their data only")
	def get_all_users_data_only(data, expected_status):
		response = action.get(ops.Api_Data.page(data))
		status = response.status_code
		print(json.dumps(response.json()['data'], indent=2), "\n")
		Verifications.verify_equals(status, expected_status)
		
	@staticmethod
	@allure.step("get a specific user")
	def get_user_by_id(number, expected_response):
		response = action.get(ops.Api_Data.id(number))
		status = response.status_code
		print(json.dumps(response.json(), indent=2), "\n")
		Verifications.verify_equals(status, expected_response)
		
	@staticmethod
	@allure.step("create a user")
	def post_user(data, expected_response):
		response = action.post(data)
		status = response.status_code
		print(json.dumps(response.json(), indent=2), "\n")
		Verifications.verify_equals(status, expected_response)
		
	@staticmethod
	@allure.step("Register a user")
	def register_user(data, expected_response):
		response = action.register(data)
		status = response.status_code
		print(response.json(), "\n")
		Verifications.verify_equals(status, expected_response)
		
	@staticmethod
	@allure.step("update a user")
	def update_user(id, data, expected_response):
		response = action.put(ops.Api_Data.id(id), data)
		status = response.status_code
		print(json.dumps(response.json(), indent=2), "\n")
		Verifications.verify_equals(status, expected_response)
		
	@staticmethod
	@allure.step("Delete a user")
	def delete_user(id, expected_response):
		response = action.delete(ops.Api_Data.id(id))
		status_code = response.status_code
		Verifications.verify_equals(status_code, expected_response)
	
	
data_file = ops.read_csv(ops.get_data('API_DDT'))
id_data = (
	(int(data_file[0][1])),
	(int(data_file[1][1])),
	(int(data_file[2][1])),
	(int(data_file[3][1])),
	(int(data_file[4][1])),
	(int(data_file[5][1]))
)
