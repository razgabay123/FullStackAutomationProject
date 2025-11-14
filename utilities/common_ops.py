import os
import csv
import allure
from pathlib import Path
from typing import Optional
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

# Load environment variables from .env file
load_dotenv()

# Mapping from XML node names to environment variable names
XML_TO_ENV_MAPPING = {
    'WaitTime': 'WAIT_TIME',
    'Browser': 'BROWSER',
    'URL': 'WEB_URL',
    'login-csv': 'LOGIN_CSV',
    'PW-browser': 'PLAYWRIGHT_BROWSER',
    'PW-URL': 'PLAYWRIGHT_URL',
    'filter_csv': 'FILTER_CSV',
    'Mobile_Device': 'MOBILE_DEVICE',
    'UDID': 'UDID',
    'App_Package': 'APP_PACKAGE',
    'App_Activity': 'APP_ACTIVITY',
    'Bundle_ID': 'BUNDLE_ID',
    'Appium_server': 'APPIUM_SERVER',
    'calculations_csv': 'CALCULATIONS_CSV',
    'swipe_dur': 'SWIPE_DURATION',
    'API_URL': 'API_URL',
    'API_DDT': 'API_DDT_CSV',
    'screenshots_path': 'SCREENSHOTS_PATH',
    'Electron_App': 'ELECTRON_APP_PATH',
    'Electron_Driver': 'ELECTRON_DRIVER_PATH',
    'Application_Name': 'APPLICATION_NAME',
    'WinAppDriver_Service': 'WINAPPDRIVER_SERVICE',
    'DB_name': 'DATABASE_PATH',
    'Host': 'PERFORMANCE_TEST_HOST',
    'API_KEY': 'API_KEY',
}


def _convert_xml_name_to_env_name(xml_name: str) -> str:
    """
    Converts XML node name to environment variable name.
    
    Args:
        xml_name: XML node name (e.g., 'PW-browser', 'login-csv')
    
    Returns:
        Environment variable name (e.g., 'PLAYWRIGHT_BROWSER', 'LOGIN_CSV')
    """
    # Check mapping first
    if xml_name in XML_TO_ENV_MAPPING:
        return XML_TO_ENV_MAPPING[xml_name]
    
    # Fallback: convert to UPPER_SNAKE_CASE
    # Replace hyphens and spaces with underscores, then uppercase
    env_name = xml_name.replace('-', '_').replace(' ', '_').upper()
    return env_name


####################
# name: wait
# waits for element to exist or display based on choice
# parameters: driver- selenium driver type, for_element - string (For enum), elem - WebElement
####################
def wait(driver, for_element, elem):
	if for_element == 'element_exists':
		WebDriverWait(driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
	elif for_element == 'element_displayed':
		WebDriverWait(driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))


####################
# name: read_csv
# reads data from csv files
# file_name: String parameter
# returns looped through strings
####################
def read_csv(file_name):
	data = []
	with open(file_name, newline='') as file:
		reader = csv.reader(file)
		for row in reader:
			data.insert(len(data), row)
		return data
	
	
####################
# Enums for selecting displayed element or exist element, the wait method uses this
#####################
class For:
	ELEMENT_EXISTS = 'element_exists'
	ELEMENT_DISPLAYED = 'element_displayed'
	
	
####################
# Save: # Enum for choosing save or not
#####################
class Save:
	# function name save:
	# r: string parameter
	# returns true or false
	@staticmethod
	def save(r):
		if r == 'yes':
			return True
		elif r == 'no':
			return False
		
		
####################
# attach_file: Function for allure screenshot attachment
# driver: selenium driver parameter
#####################
def attach_file(driver):
	image = "allure-screen-shots/screen.png"
	driver.get_screenshot_as_file(image)
	allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
	
	
#####################
# get_data: reads data from environment variables (.env) or XML file (fallback)
# Priority: Environment variable > XML file
# node_name: string parameter (XML node name)
# return a string of the node's value
#####################
def get_data(node_name: str) -> str:
	"""
	Retrieves configuration value from environment variables or XML file.
	
	Priority order:
	1. Environment variable (.env file)
	2. XML configuration file (fallback)
	
	Args:
		node_name: XML node name (e.g., 'WaitTime', 'API_URL', 'PW-browser')
	
	Returns:
		String value from environment variable or XML node.
	
	Raises:
		KeyError: If configuration not found in either environment or XML.
	"""
	# Convert XML node name to environment variable name
	env_var_name = _convert_xml_name_to_env_name(node_name)
	
	# Try to get from environment variable first
	env_value = os.getenv(env_var_name)
	if env_value:
		return env_value
	
	# Fallback to XML file
	try:
		xml_path = Path("configuration/data.xml")
		if xml_path.exists():
			root = ET.parse(str(xml_path)).getroot()
			node = root.find(f'.//{node_name}')
			if node is not None and node.text:
				return node.text
	except (FileNotFoundError, ET.ParseError, AttributeError):
		pass
	
	# If not found in either place, raise error
	raise KeyError(
		f"Configuration '{node_name}' not found. "
		f"Checked environment variable '{env_var_name}' and XML file 'configuration/data.xml'"
	)


#####################
# Api_Data: Enum for API dummy usage
#####################
class Api_Data:
	# Function name: page
	# number: int parameter
	# returns the API data at the desired page
	@staticmethod
	def page(number):
		return f"?page={number}"
	
	# Function name: id
	# id: int parameter
	# returns the API employee data at the desired id
	@staticmethod
	def id(id):
		return f"/{id}"
	
	# Function name: unknown
	# returns API colours data
	@staticmethod
	def unknown():
		return "unknown"
	
	# Function name: unknown
	# returns API colour data by id
	@staticmethod
	def unknown_id(id):
		return f"uknown/{id}"
	