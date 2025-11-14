import sqlite3
import time
import sys
import os
from pathlib import Path

# Add project root to Python path for all tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

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
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from utilities.playwright_listener import attach_playwright_listeners

driver = None
action = None
m_action = None
mobile_size = None
webdriver = get_data("Browser")
database = None


# the configuration of selenium web driver, initiates the driver + browser(s)
@pytest.fixture(scope='class')
def init_web_driver(request: pytest.FixtureRequest) -> None:
    """
    Initialize web driver for test class.
    With scope='class', this fixture runs once per test class,
    so all parametrized tests in the class share the same browser instance.
    """
    import sys
    current_module = sys.modules[__name__]
    
    # Create new driver (scope='class' ensures this only runs once per class)
    edriver = get_web_driver()
    driver_instance = EventFiringWebDriver(edriver, EventListener())
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(int(get_data('WaitTime')))
    
    # Set driver in module-level variables (for imports like conf.driver)
    setattr(current_module, 'driver', driver_instance)
    request.cls.driver = driver_instance
    
    # Set action chains
    action_instance = ActionChains(driver_instance)
    setattr(current_module, 'action', action_instance)
    
    # Also update any already-imported references
    import test_cases.conftest
    test_cases.conftest.driver = driver_instance
    test_cases.conftest.action = action_instance
    
    ManagePages.init_web_pages()
    yield
    # Clean up - close browser after all tests in class complete
    time.sleep(1)
    try:
        if driver_instance:
            driver_instance.quit()
    except Exception:
        pass
    finally:
        # Clean up module variables
        setattr(current_module, 'driver', None)
        setattr(current_module, 'action', None)
        test_cases.conftest.driver = None
        test_cases.conftest.action = None


@pytest.fixture(scope='class')
def init_playwright_driver(request: pytest.FixtureRequest) -> None:
    p, browser, context, page = get_playwright_driver()
    attach_playwright_listeners(page)
    globals()['driver'] = page
    request.cls.driver = page
    request.cls.context = context  # Make context available for screenshots/tracing
    yield
    # Stop tracing and save it
    context.tracing.stop(path="test-results/trace.zip")
    browser.close()
    p.stop()


# the configuration of Appium driver, initiates the driver + App
@pytest.fixture(scope='class')
def init_mobile_driver(request: pytest.FixtureRequest) -> None:
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
def init_electron_driver(request: pytest.FixtureRequest) -> None:
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
def init_desktop_driver(request: pytest.FixtureRequest) -> None:
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
def init_db_connection(request: pytest.FixtureRequest) -> None:
    my_db = get_data("DB_name")
    try:
        db = sqlite3.connect(my_db)
        from extensions.DB_actions import DB_Actions
        DB_Actions.database = db
        request.cls.database = db
        
        # Verify database connection by executing a simple query
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        if not tables:
            raise Exception("Database exists but contains no tables")
            
        yield
        db.close()
    except sqlite3.Error as e:
        pytest.fail(f"Failed to connect to database {my_db}: {str(e)}")
    except Exception as e:
        pytest.fail(f"Database error: {str(e)}")


# boots browser data dependant (data.xml)
def get_web_driver() -> selenium.webdriver.Remote:
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
def get_mobile_driver() -> appium.webdriver.Remote:
    if get_data('Mobile_Device').lower() == 'android':
        driver = get_android(get_data('UDID'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver = get_ios(get_data('UDID'))
    else:
        driver = None
        raise Exception("error: unsupported mobile system")
    return driver


# boots Electron data dependant (data.xml)
def get_electron_driver() -> selenium.webdriver.Remote:
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("Electron_App")
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("Electron_Driver"))
    return driver


# boots WinApp data dependant (data.xml)
def get_desktop_driver() -> appium.webdriver.Remote:
    dc = {}
    dc['app'] = get_data("Application_Name")
    dc['platforName'] = 'Windows'
    dc["deviceName"] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
    return driver


# function to boot Chrome browsers
def get_chrome() -> selenium.webdriver.Remote:
    options = selenium.webdriver.ChromeOptions()
    # Check if headless mode should be enabled (from .env or XML, default to False for debugging)
    headless_mode = os.getenv('HEADLESS', 'false').lower() == 'true'
    if headless_mode:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    # Add user agent to avoid detection as bot
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    chrome_driver = selenium.webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return chrome_driver


# function to boot FF browsers
def get_firefox() -> selenium.webdriver.Remote:
    ff_driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return ff_driver


# function to boot Edge browsers
def get_edge() -> selenium.webdriver.Remote:
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


def get_playwright_driver() -> tuple[sync_playwright, Browser, BrowserContext, Page]:
    p = sync_playwright().start()
    browser_type = get_data('PW-browser').lower()
    if browser_type == "chrome" or browser_type == "chromium":
        browser = p.chromium.launch(headless=True, channel="chrome", slow_mo=int(get_data('WaitTime')) * 250)
    elif browser_type == "firefox":
        browser = p.firefox.launch(headless=True, slow_mo=int(get_data('WaitTime')) * 250)
    elif browser_type == "webkit":
        browser = p.webkit.launch(headless=True, slow_mo=int(get_data('WaitTime')) * 250)
    else:
        raise Exception("Unsupported Playwright browser")
    
    # Enhanced context with native Playwright features
    context = browser.new_context(
        record_video_dir="test-results/videos/",  # Record videos
        record_video_size={"width": 1280, "height": 720},
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True  # Handle SSL issues in Docker
    )
    
    # Start tracing for better debugging
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    ManagePages.init_pw_web_pages(page)
    page.set_default_timeout(int(get_data('WaitTime')) * 5000)
    page.goto(get_data("PW-URL"))
    return p, browser, context, page


# function to boot android devices
def get_android(udid: str) -> appium.webdriver.Remote:
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    # Get Appium server URL from environment variables or fallback to data.xml
    # Priority: APPIUM_SERVER (full URL) > APPIUM_HOST + APPIUM_PORT > XML
    appium_server = os.getenv('APPIUM_SERVER')
    if appium_server:
        appium_url = appium_server
    else:
        appium_host = os.getenv('APPIUM_HOST', 'localhost')
        appium_port = os.getenv('APPIUM_PORT', '4723')
        appium_url = f"http://{appium_host}:{appium_port}/wd/hub"
    
    android_driver = appium.webdriver.Remote(appium_url, dc)
    return android_driver


# function to boot Apple devices
def get_ios(udid) -> appium.webdriver.Remote:
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    # Get Appium server URL from environment variables or fallback to data.xml
    # Priority: APPIUM_SERVER (full URL) > APPIUM_HOST + APPIUM_PORT > XML
    appium_server = os.getenv('APPIUM_SERVER')
    if appium_server:
        appium_url = appium_server
    else:
        appium_host = os.getenv('APPIUM_HOST', 'localhost')
        appium_port = os.getenv('APPIUM_PORT', '4723')
        appium_url = f"http://{appium_host}:{appium_port}/wd/hub"
    
    ios_driver = appium.webdriver.Remote(appium_url, dc)
    return ios_driver
