from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#************* scenario 1 ******************************** #

@when('we visit treevolution/config')
def step(context):
    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')

@then('i looking for value for range type and comparing it sould be different')
def step(context):
    TreeNumber = context.browser.find_element(By.ID, "inputTreeNumber").get_attribute('value')
    New_TreeNumber = context.browser.execute_script("document.getElementById('inputTreeNumber').setAttribute('value', '25')")
    assert TreeNumber != New_TreeNumber
    
