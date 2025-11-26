from locust import HttpUser, task, constant
from utilities.common_ops import get_data
# Import simple reporting (this will automatically set up event listeners)
import test_cases.test_performance.simple_listener


class MyReqRes(HttpUser):
    host = get_data("Host")  # Load the host URL from external configuration
    weight = 2
    wait_time = constant(1)

    def on_start(self):
        # Set up your API key - you can also load this from environment variables
        self.api_key = get_data("API_KEY")  # Load the API key from external configuration
        # Set up headers that will be used for all requests
        self.client.headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }

    @task(3)
    def get_users(self):
        # Example of a GET request to fetch users
        with self.client.get("/api/users", name="Get Users List") as response:
            # Check for successful response
            if response.status_code != 200:
                response.failure(f"Failed to get users: {response.status_code}")
            else:
                # print the response JSON for debugging purposes
                print(response.json())

    @task(2)
    def get_single_user(self):
        # Example of a GET request to fetch a single user
        with self.client.get("/api/users/2", name="Get Single User") as response:
            # Check for successful response
            if response.status_code != 200:
                response.failure(f"Failed to get single user: {response.status_code}")
            else:
                # print the response JSON for debugging purposes
                print(response.json())

    @task(1)
    def create_user(self):
        # Example of a POST request to create a new user
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        with self.client.post("/api/users", json=payload, name="Create User") as response:
            # Check for successful response
            if response.status_code != 201:
                response.failure(f"Failed to create user: {response.status_code}")
            else:
                # print the response JSON for debugging purposes
                print(response.json())
# Last updated: 2025-11-26
