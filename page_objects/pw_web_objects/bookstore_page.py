from playwright.sync_api import Page, Locator

# books = '//*[@id="productList"]/li'


class BookstorePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def search_input(self) -> Locator:
        return self.page.locator("#searchBar")

    @property
    def books(self) -> Locator:
        return self.page.locator('#productList li:visible')

    def get_visible_book_count(self) -> int:
        return self.books.count()
