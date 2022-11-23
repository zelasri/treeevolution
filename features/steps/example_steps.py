from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I navigate to the PyPi Home page')
def step_impl(context):
    context.browser.get("https://pypi.org")
    assert "PyPI" in context.browser.title

@when('I search for "{search_term}"')
def step_impl(context, search_term):
    context.browser.find_element(By.ID, "search").send_keys(search_term)
    context.browser.find_element(By.ID, "search").send_keys(Keys.ENTER)

@then('I find a link to project "{search_result}"')
def step_impl(context, search_result):
    selector = f'a[href="/project/{search_result}/"]'
    assert context.browser.find_element(By.CSS_SELECTOR, selector)

@step('If I click on project "{search_result}", I find its version "{version}"')
def step_impl(context, search_result, version):
    selector = f'a[href="/project/{search_result}/"]'
    context.browser.find_element(By.CSS_SELECTOR, selector).click()
    behave_version = context.browser.find_element(By.TAG_NAME, "h1").text.strip()
    assert behave_version == f"behave {version}"