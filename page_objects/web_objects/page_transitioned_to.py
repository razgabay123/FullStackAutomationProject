from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
hero_title = (By.TAG_NAME, "h1")


# finds the imdb hero title, eg: thor
class Transitioned_Page():
	def __init__(self, driver) -> None:
		self.driver = driver
		
	def get_hero_title(self) -> WebElement:
		return self.driver.find_element(hero_title[0], hero_title[1])
	