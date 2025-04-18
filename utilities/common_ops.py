import csv
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET


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
	image = r"D:\Automation\test_automation_final_project\allure-screen-shots/screen.png"
	driver.get_screenshot_as_file(image)
	allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
	
	
#####################
# get_data: reads data from external xml
# node_name: string parameter
# return a string of the node's value
#####################
def get_data(node_name):
	root = ET.parse(r"D:\Automation\test_automation_final_project\configuration\data.xml").getroot()
	return root.find('.//' + node_name).text


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
	