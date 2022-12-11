import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@when('Le nombre d’espèces d’arbres sélectionné est le même que la configuration')
def step_impl(context):
    

    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')
    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-10-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2030-12-18')")
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2030-12-18')")
    
    context.browser.execute_script("document.getElementById('inputDaysNumber').setAttribute('value', '10')")

    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    firstopt = Ash.first_selected_option
    selectedkind_tree = firstopt.text 

    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    #onglet simulation
    context.browser.implicitly_wait(10)
    context.browser.get("http://127.0.0.1:5000/")
    context.browser.get("http://127.0.0.1:5000/simulation")
    context.browser.implicitly_wait(10)
    # cliquer sur le button initSimulation
    init=context.browser.find_element(By.ID,"initSimulationBtn")
    init.click()
    #//*[@id="configurationPanel"]/table/tbody/tr[5]/td[2]
    Kinds=context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[5]/td[2]").text
    assert Kinds in selectedkind_tree
