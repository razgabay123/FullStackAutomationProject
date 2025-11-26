import os
import allure
import requests
from dotenv import load_dotenv
from utilities.common_ops import get_data

# Load environment variables
load_dotenv()

# Get API key from environment variable, fallback to get_data() for XML compatibility
try:
    API_KEY = os.getenv("API_KEY") or get_data("API_KEY")
except KeyError:
    # If not found in either place, use default (for backward compatibility)
    API_KEY = "reqres-free-v1"

headers = {
	"x-api-key": API_KEY
}


class API_Actions:
	@staticmethod
	@allure.step("get API data")
	def get(data) -> requests.Response:
		response = requests.get(f"{get_data('API_URL')}users{data}", headers=headers)
		return response
	
	@staticmethod
	@allure.step("create API data")
	def post(data) -> requests.Response:
		response = requests.post(f"{get_data('API_URL')}users", json=data, headers=headers)
		return response
	
	@staticmethod
	@allure.step("register a user")
	def register(data) -> requests.Response:
		response = requests.post(f"{get_data('API_URL')}register", json=data, headers=headers)
		return response
	
	@staticmethod
	@allure.step("update API data")
	def put(id, data) -> requests.Response:
		response = requests.put(f"{get_data('API_URL')}users/{id}", json=data, headers=headers)
		return response
	
	@staticmethod
	@allure.step("delete API data")
	def delete(data) -> requests.Response:
		response = requests.delete(f"{get_data('API_URL')}users{data}", headers=headers)
		return response
# Last updated: 2025-11-26
