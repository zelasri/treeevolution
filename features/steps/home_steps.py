from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@when('we visit treevolution')
def step(context):
   context.browser.get('http://127.0.0.1:5000')

@then('it should have a title "Welcome to the Treevolution simulator"')
def step(context):
    myElement = context.browser.find_element(By.TAG_NAME, "h2")
    assert myElement.text == "Welcome to the Treevolution simulator"


