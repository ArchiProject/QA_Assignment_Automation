from behave import when, then
from features.pages.search_page import SearchPage

@when('I search for "{term}"')
def step_search_for_term(context, term):
    context.search_page = SearchPage(context.page)  # Pass context.page directly to SearchPage
    context.search_page.open()  # Now use context.page for interaction
    context.search_page.enter_search_term(term)
    context.search_term = term.strip()

@when('I search with an empty string')
def step_search_empty(context):
    context.search_page = SearchPage(context.page)  # Pass context.page directly to SearchPage
    context.search_page.open()
    context.search_page.enter_search_term("")

@then('I should see relevant results for "{term}"')
def step_check_results(context, term):
    page_text = context.search_page.get_results_text()
    assert term.lower() in page_text.lower()

@then("I should be prompted to enter a search term")
def step_prompt_displayed(context):
    assert context.search_page.is_prompt_displayed()

@then("I should see a message indicating no results were found")
def step_no_results(context):
    page_text = context.search_page.get_results_text()
    assert "no results" in page_text.lower() or "لم يتم العثور" in page_text  # Arabic fallback

@then("the input should be sanitized")
def step_input_sanitized(context):
    assert context.search_page.is_input_sanitized()
