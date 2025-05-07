from playwright.sync_api import Page
from features.locators import SearchPageLocators
import os
class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://sdaia.gov.sa/en/Search/Pages/advanced.aspx"
            # "https://sdaia.gov.sa/en/Search/Pages/results.aspx"
            # "https://sdaia.gov.sa/en/default.aspx"
                   # "https://sdaia.gov.sa/en/Search/Pages/default.aspx"

    def open(self):
        self.page.goto(self.url)  # Navigate to the URL
        # search_button = self.page.get_by_role("button", name="Search")
        # search_button.click()
    def enter_search_term(self, term):
        # search_input = self.page.locator('input[placeholder="Enter the search term..."]')
        search_input = self.page.locator('//html/body/form/div[5]/div[2]/div/div[4]/div[1]/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/input')
        search_input.fill(term)
        search_button = self.page.locator('#ctl00_ctl56_g_f5f4be33_a4c2_448e_9296_a1e3625f1cfb_ASB_BS_SRCH_1')
        search_button.click()
        # search_input.fill(term)  # Fill the search input field
        # search_input.press('Enter')  # Simulate pressing the "Enter" key

    def get_results_text(self):
        return self.page.content()  # Get page content

    def is_prompt_displayed(self):
        return "Please enter a search term" in self.page.content()

    def is_input_sanitized(self):
        return "<script>" not in self.page.content()
