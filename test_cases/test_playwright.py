import pytest
import workflows.playwright_flows as flow


@pytest.mark.usefixtures("init_playwright_driver")
class TestPlayWright:
    @pytest.mark.sanity
    def test_01_stabilize_connection(self):
        """Sanity test: check successful connection"""
        # Take a screenshot to verify page loaded
        self.driver.screenshot(path="test-results/screenshots/connection_test.png")
        print('\nsuccess')

    def test_02_basic_search(self):
        """Basic search functionality test"""
        # Take screenshot before action
        self.driver.screenshot(path="test-results/screenshots/before_search.png")
        flow.PlaywrightFlows.fill_search_bar("Agile")
        # Take screenshot after action
        self.driver.screenshot(path="test-results/screenshots/after_search.png")

    def test_03_verify_books_amount(self):
        """Filter and verify the number of books shown"""
        flow.PlaywrightFlows.fill_search_bar("Java")
        # Screenshot before verification
        self.driver.screenshot(path="test-results/screenshots/java_books_filtered.png")
        flow.PlaywrightFlows.verify_shown_books(3)

    @pytest.mark.parametrize('value,shown', flow.filter_data)
    def test_04_ddt_filtering(self, value, shown):
        """Data-driven test: filter books and verify count"""
        flow.PlaywrightFlows.fill_search_bar(value)
        # Screenshot with dynamic filename based on test data
        self.driver.screenshot(path=f"test-results/screenshots/ddt_filter_{value.lower().replace(' ', '_')}.png")
        flow.PlaywrightFlows.verify_shown_books(int(shown))
