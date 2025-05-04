import sqlite3
import time

import allure
import pytest
import selenium.webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import appium.webdriver

from utilities.common_ops import get_data
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from playwright.sync_api import sync_playwright

from utilities.playwright_listener import attach_playwright_listeners

driver = None
action = None
m_action = None
mobile_size = None
webdriver = get_data("Browser")
database = None


# the configuration of selenium web driver, initiates the driver + browser(s)
@pytest.fixture(scope='class')
def init_web_driver(request):
	edriver = get_web_driver()
	globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
	driver = globals()['driver']
	driver.maximize_window()
	driver.implicitly_wait(int(get_data('WaitTime')))
	request.cls.driver = driver
	globals()['action'] = ActionChains(driver)
	ManagePages.init_web_pages()
	yield
	time.sleep(2)
	driver.quit()


@pytest.fixture(scope='class')
def init_playwright_driver(request):
	p, browser, context, page = get_playwright_driver()
	attach_playwright_listeners(page)
	globals()['driver'] = page
	request.cls.driver = page
	  # or a new method like init_playwright_pages() if needed
	yield
	browser.close()
	p.stop()


# the configuration of Appium driver, initiates the driver + App
@pytest.fixture(scope='class')
def init_mobile_driver(request):
	edriver = get_mobile_driver()
	globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
	driver = globals()['driver']
	driver.implicitly_wait(int(get_data(('WaitTime'))))
	request.cls.driver = driver
	globals()['m_action'] = TouchAction(driver)
	request.cls.m_action = globals()['m_action']
	globals()['mobile_size'] = driver.get_window_size()
	request.cls.mobile_size = globals()['mobile_size']
	ManagePages.init_mobile_pages()
	yield
	driver.quit()


# the configuration of Electron driver, initiates the driver + app
@pytest.fixture(scope='class')
def init_electron_driver(request):
	edriver = get_electron_driver()
	globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
	driver = globals()['driver']
	driver.implicitly_wait(int(get_data(('WaitTime'))))
	request.cls.driver = driver
	globals()['action'] = ActionChains(driver)
	request.cls.action = globals()['action']
	ManagePages.init_electron_pages()
	yield
	driver.quit()


# the configuration of WinApp driver, initiates the driver + app
@pytest.fixture(scope="class")
def init_desktop_driver(request):
	edriver = get_desktop_driver()
	globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
	driver = globals()['driver']
	driver.implicitly_wait(int(get_data(('WaitTime'))))
	request.cls.driver = driver
	ManagePages.init_desktop_pages()
	yield
	driver.quit()


# the configuration of SQL database connection
@pytest.fixture(scope="class")
def init_db_connection(request):
	my_db = get_data("DB_name")
	db = sqlite3.connect(my_db)

	from extensions.DB_actions import DB_Actions
	DB_Actions.database = db

	request.cls.database = db
	yield
	db.close()


# boots browser data dependant (data.xml)
def get_web_driver():
	if webdriver.lower() == 'chrome':
		driver = get_chrome()
	elif webdriver.lower() == 'firefox':
		driver = get_firefox()
	elif webdriver.lower() == 'edge':
		driver = get_edge()
	else:
		driver = None
		raise Exception('wrong input or unrecognized browser')
	return driver


# boots mobile data dependant (data.xml)
def get_mobile_driver():
	if get_data('Mobile_Device').lower() == 'android':
		driver = get_android(get_data('UDID'))
	elif get_data('Mobile_Device').lower() == 'ios':
		driver = get_ios(get_data('UDID'))
	else:
		driver = None
		raise Exception("error: unsupported mobile system")
	return driver


# boots Electron data dependant (data.xml)
def get_electron_driver():
	options = selenium.webdriver.ChromeOptions()
	options.binary_location = get_data("Electron_App")
	driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("Electron_Driver"))
	return driver


# boots WinApp data dependant (data.xml)
def get_desktop_driver():
	dc = {}
	dc['app'] = get_data("Application_Name")
	dc['platforName'] = 'Windows'
	dc["deviceName"] = 'WindowsPC'
	driver = appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
	return driver


# function to boot Chrome browsers
def get_chrome():
	chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
	return chrome_driver


# function to boot FF browsers
def get_firefox():
	ff_driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
	return ff_driver


# function to boot Edge browsers
def get_edge():
	edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
	return edge_driver


def get_playwright_driver():
	p = sync_playwright().start()
	browser_type = get_data('PW-browser').lower()
	if browser_type == "chrome" or browser_type == "chromium":
		browser = p.chromium.launch(headless=False, channel="chrome", slow_mo=int(get_data('WaitTime')) * 250)
	elif browser_type == "firefox":
		browser = p.firefox.launch(headless=False, slow_mo=int(get_data('WaitTime')) * 250)
	elif browser_type == "webkit":
		browser = p.webkit.launch(headless=False, slow_mo=int(get_data('WaitTime')) * 250)
	else:
		raise Exception("Unsupported Playwright browser")
	context = browser.new_context()
	page = context.new_page()
	ManagePages.init_pw_web_pages(page)
	page.set_default_timeout(int(get_data('WaitTime')) * 5000)
	page.goto(get_data("PW-URL"))
	return p, browser, context, page


# function to boot android devices
def get_android(udid):
	dc = {}
	dc['udid'] = udid
	dc['appPackage'] = get_data('App_Package')
	dc['appActivity'] = get_data('App_Activity')
	dc['platformName'] = 'android'
	android_driver = appium.webdriver.Remote(get_data('Appium_server'), dc)
	return android_driver


# function to boot Apple devices
def get_ios(udid):
	dc = {}
	dc['udid'] = udid
	dc['bundle_id'] = get_data('Bundle_ID')
	dc['platformName'] = 'ios'
	ios_driver = appium.webdriver.Remote(get_data('Appium_server'), dc)
	return ios_driver
