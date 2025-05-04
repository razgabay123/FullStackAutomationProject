
from page_objects.mobile_objects.calculator_page import Calculator_Page
from page_objects.web_objects.login_page import Login_Page
from page_objects.electron_objects.todolist_page import TaskPage
import test_cases.conftest as conf
from page_objects.web_objects.main_page import Main_Page
from page_objects.web_objects.page_transitioned_to import Transitioned_Page
from page_objects.mobile_objects.saved_calculations_page import Saved_Calculations_Page
from page_objects.desktop_objects.calculator_app import Calculator
from page_objects.pw_web_objects.bookstore_page import BookstorePage

# Web Objects
web_login = None
web_main = None
web_transition = None
pw_web_bookstore = None

# Mobile Objects
mobile_calculator = None
saved_calculations = None

# Electron Objects
todolist = None

# Desktop Objects
calculator = None


# groups all the objects in one place, for easier usage
class ManagePages:
	# web
	@staticmethod
	def init_web_pages():
		globals()['web_main'] = Main_Page(conf.driver)
		globals()['web_login'] = Login_Page(conf.driver)
		globals()['web_transition'] = Transitioned_Page(conf.driver)

	# playwright-web
	@staticmethod
	def init_pw_web_pages(driver):
		globals()['pw_web_bookstore'] = BookstorePage(driver)

	# mobile
	@staticmethod
	def init_mobile_pages():
		globals()['mobile_calculator'] = Calculator_Page(conf.driver)
		globals()['saved_calculations'] = Saved_Calculations_Page(conf.driver)
	
	# electron
	@staticmethod
	def init_electron_pages():
		globals()['todolist'] = TaskPage(conf.driver)
	
	# desktop
	@staticmethod
	def init_desktop_pages():
		globals()['calculator'] = Calculator(conf.driver)
		