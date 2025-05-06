from playwright.sync_api import sync_playwright
from behave import *

def before_all(context):
    # Start Playwright and launch browser
    playwright = sync_playwright().start()
    context.playwright = playwright  # Store playwright instance in context (for use in after_all)
    context.browser = playwright.chromium.launch(headless=True)  # Launch Chromium browser
    context.page = context.browser.new_page()  # Create a new browser page

def after_all(context):
    # Close the browser and playwright instance after all tests are done
    if context.page:
        context.page.close()
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
