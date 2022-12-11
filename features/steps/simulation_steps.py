import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@when ('enter info in configuration')
def  step_impl(context):
    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')
    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    firstopt = Ash.first_selected_option
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-10-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2030-02-15')")

    # recuperer la valeur  de span et input de nombre des arbres
    numbertree_text_conf = context.browser.find_element(By.ID,"treeNumber").text
    numbertree_input_conf = context.browser.find_element(By.ID,"inputTreeNumber").get_attribute('value')

    # recuperer la valeur  de span et input de nombre des joures
    numberdays_text_conf = context.browser.find_element(By.ID, "daysNumber").text
    numberdays_conf = context.browser.find_element(By.ID, "inputDaysNumber").get_attribute('value')

    date_begin = context.browser.find_element(By.ID, "inputStartDate").get_attribute('value')
    date_end = context.browser.find_element(By.ID, "inputEndDate").get_attribute('value')

    
    #tester si la valeur  de span et input de nombre des arbres et des joures sont identiques
    assert firstopt.text == 'Ash (treevolution.models.trees.oak.Ash)'
    assert date_begin ==  '2022-10-04'
    assert date_end == '2030-02-15'
    assert numbertree_text_conf == numbertree_input_conf 
    assert numberdays_conf == numberdays_text_conf
    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    context.browser.get('http://127.0.0.1:5000/simulation')
    #runSimulationBtn
    button=context.browser.find_element(By.ID,"initSimulationBtn")
    button.click()
    context.browser.set_page_load_timeout(10)

    Treehumus=context.browser.find_element(By.XPATH,"//div[@id='legendPanel']/table/tbody/tr[2]/td[2]").text
    assert "0 (humus)" in Treehumus

    Seeds=context.browser.find_element(By.XPATH,"//*[@id='legendPanel']/table/tbody/tr[3]/td[1]").text
    assert "0" in Seeds
