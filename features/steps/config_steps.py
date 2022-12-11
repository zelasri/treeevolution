from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#************* scenario 1 ******************************** #

@when('we visit treevolution/config')
def step(context):
    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')

@when('date of end of simulation  inferior of begin date')
def step(context):
    #document.getElementById('inputKindsTree').getElementsByTagName('option')[0].selected = 'selected'

    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')   
    # insertion de date de debut
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-12-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2022-10-18')")
    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
  
@then ('Invalid start date and end date')
def step_impl(context):
    alert=context.browser.find_element(By.CLASS_NAME, "alert").text
    assert "Invalid start date and end date." in alert
