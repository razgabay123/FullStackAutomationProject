from playwright.sync_api import Locator


class PlayWrightActions:
    @staticmethod
    def click_element(locator: Locator):
        locator.click()

    @staticmethod
    def fill_input(locator: Locator, value: str):
        locator.fill(value)

    @staticmethod
    def wait_for_element(locator: Locator, timeout: int = 5000):
        locator.wait_for(state="visible", timeout=timeout)
