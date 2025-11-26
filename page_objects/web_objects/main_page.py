from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
ironman = (By.ID, "iron_man")
captain_america = (By.ID, "captain_america")
hulk = (By.ID, "the_hulk")
thor = (By.ID, "thor")


# finds each hero clickable picture
class Main_Page():
	def __init__(self, driver) -> None:
		self.driver = driver
		
	def get_ironman(self) -> WebElement:
		return self.driver.find_element(ironman[0], ironman[1])
	
	def get_captain_america(self) -> WebElement:
		return self.driver.find_element(captain_america[0], captain_america[1])
	
	def get_hulk(self) -> WebElement:
		return self.driver.find_element(hulk[0], hulk[1])
	
	def get_thor(self) -> WebElement:
		return self.driver.find_element(thor[0], thor[1])
# Last updated: 2025-11-26
