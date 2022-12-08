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


#****************************** scenerio 6 *******************************#

@when('Le nombre d’espèces d’arbres sélectionné est le même que la configuration')
def step_impl(context):
    

    context.browser.get('http://127.0.0.1:5000')
    context.browser.get('http://127.0.0.1:5000/config')
    Ash = Select(context.browser.find_element(By.ID,'inputKindsTree'))
    Ash.select_by_visible_text('Ash (treevolution.models.trees.oak.Ash)')
    context.browser.execute_script("document.getElementById('inputStartDate').setAttribute('value', '2022-10-04')")
    # insertion de date de fin
    context.browser.execute_script("document.getElementById('inputEndDate').setAttribute('value', '2023-12-18')")
    
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

#****************************** scenerio 7 *******************************#

    
@when('la date et le nombre d’arbres ont évolué après un certain délai')
def step_impl(context):
    context.browser.get("http://127.0.0.1:5000/")
    context.browser.get("http://127.0.0.1:5000/simulation")

    numberTreebegin =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[2]/td[2]").text
    assert numberTreebegin == '1'
    begindate =context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[3]/td[2]").text
    assert begindate == '2022-10-04'
    #//*[@id="configurationPanel"]/table/tbody/tr[2]/td[2]
    #//*[@id='configurationPanel']/table/tbody/tr[3]/td[2]
    initSimulationBtn=context.browser.find_element(By.ID,"initSimulationBtn")
    initSimulationBtn.click()
    context.browser.implicitly_wait(10)

    numbretree_atbegin = context.browser.find_element(By.XPATH,"//*[@id='configurationPanel']/table/tbody/tr[2]/td[2]").text
    assert numbretree_atbegin == '1'

    runSimulationBtn=context.browser.find_element(By.ID,"runSimulationBtn")
    runSimulationBtn.click()
    time.sleep(30)
    runSimulationBtn.click()
    legend = context.browser.find_element(By.XPATH,"//*[@id='legendTitle']/div/div[1]").text
    assert legend !=  begindate

    #//*[@id="legendPanel"]/table/tbody/tr[2]/td[1]/text()
    nbTrees = context.browser.find_element(By.XPATH,"//div[@id='legendPanel']/table/tbody/tr[2]/td").text

    assert nbTrees !=  numbretree_atbegin

    #//*[@id="configurationPanel"]/table/tbody/tr[2]/td[2]
    
@when('Story9')
def step_impl(context):
        context.browser.get("http://127.0.0.1:5000/")
        context.browser.get("http://127.0.0.1:5000/simulation")

        initSimulationBtn=context.browser.find_element(By.ID,"initSimulationBtn")
        initSimulationBtn.click()
        runSimulationBtn = context.browser.find_element(By.ID,"runSimulationBtn")
        # lancer la simulation
        runSimulationBtn.click()
        time.sleep(10)
        #arreter la simulation
        runSimulationBtn.click()
        # verfier que la simulation a progressé
        progress = context.browser.find_element(By.ID,"simulationProgress").text
        assert progress != '0%'
        #réinitialiser la simulation
        initSimulationBtn.click()
        #verfier que la progression de la simulation reintialise a 0
        progress = context.browser.find_element(By.ID,"simulationProgress").text
        assert progress == '0%'


    



