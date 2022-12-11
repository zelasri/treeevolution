from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#************* scenario 4 ******************************** #

@when('we visit treevolution/config')
def step(context):
    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')

@when ('enter valid start date and end date')
def  step_impl(context):
    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')
    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-10-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2022-12-18')")
    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

@then ('valid message')
def step_impl(context):
    #/html/body/div/div[1]/div/text()
    alert=context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div").text
    assert "Configuration has been updated. The simulation has been reset" in alert
    
