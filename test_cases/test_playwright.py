import pytest
import allure
import workflows.playwright_flows as flow


@pytest.mark.usefixtures("init_playwright_driver")
class TestPlayWright:
    @allure.title("test 01: sanity, check successful connection")
    @pytest.mark.sanity
    def test_01_stabilize_connection(self):
        print('\nsuccess')

    @allure.title("test 02: basic search")
    def test_02_basic_search(self):
        flow.PlaywrightFlows.fill_search_bar("Agile")

    @allure.title("test 03: filter and check how many books are shown")
    def test_03_verify_books_amount(self):
        flow.PlaywrightFlows.fill_search_bar("Java")
        flow.PlaywrightFlows.verify_shown_books(3)

    @allure.title("test 04: filter books via ddt, & verify books number shown")
    @pytest.mark.parametrize('value,shown', flow.filter_data)
    def test_04_ddt_filtering(self, value, shown):
        flow.PlaywrightFlows.fill_search_bar(value)
        flow.PlaywrightFlows.verify_shown_books(int(shown))
