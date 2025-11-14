from playwright.sync_api import Page
from selenium.webdriver.remote.webelement import WebElement
# books = '//*[@id="productList"]/li'


class BookstorePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def search_input(self) -> WebElement:
        return self.page.locator("#searchBar")

    @property
    def books(self) -> WebElement:
        return self.page.locator('#productList li:visible')

    def get_visible_book_count(self) -> int:
        return self.books.count()