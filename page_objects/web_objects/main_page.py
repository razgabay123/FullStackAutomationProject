from selenium.webdriver.common.by import By

ironman = (By.ID, "iron_man")
captain_america = (By.ID, "captain_america")
hulk = (By.ID, "the_hulk")
thor = (By.ID, "thor")


# finds each hero clickable picture
class Main_Page():
	def __init__(self, driver):
		self.driver = driver
		
	def get_ironman(self):
		return self.driver.find_element(ironman[0], ironman[1])
	
	def get_captain_america(self):
		return self.driver.find_element(captain_america[0], captain_america[1])
	
	def get_hulk(self):
		return self.driver.find_element(hulk[0], hulk[1])
	
	def get_thor(self):
		return self.driver.find_element(thor[0], thor[1])

	