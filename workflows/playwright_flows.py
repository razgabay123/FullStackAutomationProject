import utilities.common_ops as ops
from extensions.playwright_ui_actions import PlayWrightActions as action
import utilities.manage_pages as pages
from extensions.verifications import Verifications


class PlaywrightFlows:
    @staticmethod
    def fill_search_bar(value):
        """Fill the search bar with the given value"""
        action.fill_input(pages.pw_web_bookstore.search_input, value)

    @staticmethod
    def verify_shown_books(number):
        """Verify the number of books shown on the page"""
        shown_books = pages.pw_web_bookstore.get_visible_book_count()
        Verifications.verify_equals(shown_books, number)


# data extraction from csv
books_data = ops.read_csv(ops.get_data('filter_csv'))
filter_data = [
            (books_data[0][0], books_data[0][1]),
            (books_data[1][0], books_data[1][1]),
            (books_data[2][0], books_data[2][1]),
            (books_data[3][0], books_data[3][1]),
            (books_data[4][0], books_data[4][1]),
            (books_data[5][0], books_data[5][1]),
            ]
