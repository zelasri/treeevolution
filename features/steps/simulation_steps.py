import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




#****************************** scenerio 9 *******************************#

    
@when('story 9')
def step_impl(context):
    context.browser.get("http://127.0.0.1:5000/")
    context.browser.get('http://127.0.0.1:5000/config')
    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-10-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2023-12-18')")
    
    context.browser.execute_script("document.getElementById('inputDaysNumber').setAttribute('value', '10')")
    context.browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()


    context.browser.get("http://127.0.0.1:5000/simulation")
    # Information:Current configuration 

    numberTreebegin =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[2]/td[2]").text
    begindate =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[3]/td[2]").text
  

    initSimulationBtn=context.browser.find_element(By.ID,"initSimulationBtn")
    initSimulationBtn.click()

    runSimulationBtn=context.browser.find_element(By.ID,"runSimulationBtn")
    runSimulationBtn.click()

    context.browser.implicitly_wait(10)
    time.sleep(10)

    #verfier La date et le nombre d’arbres sont restés fixes après la fin de cette simulation

    progress = context.browser.find_element(By.XPATH,"//*[@id='simulationProgress']").text
    assert  '100%'in progress

    numberTreebegin_aftersimul =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[2]/td[2]").text
    begindate_afetrsimul =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[3]/td[2]").text
    #verifier l'egalité du nombre des arbres de configuration reste fixe apres la simulation
    assert numberTreebegin_aftersimul == numberTreebegin

    #verifier l'egalité du date de debut du simulation   reste fixe apres la simulation de config panel
    assert begindate == begindate_afetrsimul

    #verifier l'evolution du date de debut du simulation  panel

    legend = context.browser.find_element(By.XPATH,"//*[@id='legendTitle']/div/div[1]").text

    assert legend !=  begindate
    # apres initialistaion de la date  configuration identique avec de la simulation
    initSimulationBtn=context.browser.find_element(By.XPATH,"//*[@id='initSimulationBtn']")
    
    initSimulationBtn.click() 
   
    context.browser.implicitly_wait(10)
    assert begindate in legend

   

    #//*[@id="configurationPanel"]/table/tbody/tr[2]/td[2]
    
