from playwright.sync_api import Locator


class PlayWrightActions:
    @staticmethod
    def click_element(locator: Locator) -> None:
        locator.click()

    @staticmethod
    def fill_input(locator: Locator, value: str) -> None:
        locator.fill(value)

    @staticmethod
    def wait_for_element(locator: Locator, timeout: int = 5000) -> None:
        locator.wait_for(state="visible", timeout=timeout)
# Last updated: 2025-11-26
