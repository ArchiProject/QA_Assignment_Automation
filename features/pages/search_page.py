from playwright.sync_api import Page
from features.locators import SearchPageLocators
import os
class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://sdaia.gov.sa/en/Search/Pages/default.aspx"

    def open(self):
        self.page.goto(self.url)  # Navigate to the URL

    def enter_search_term(self, term):
        search_input = self.page.locator(SearchPageLocators.SEARCH_INPUT_ADVANCED)
        search_input.fill(term)  # Fill the search input field
        search_input.press('Enter')  # Simulate pressing the "Enter" key

    def get_results_text(self):
        return self.page.content()  # Get page content

    def is_prompt_displayed(self):
        return "Please enter a search term" in self.page.content()

    def is_input_sanitized(self):
        return "<script>" not in self.page.content()
