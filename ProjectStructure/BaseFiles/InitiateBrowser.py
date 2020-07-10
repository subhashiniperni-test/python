from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import configReader


def startBrowser():
    global driver
    if((configReader.readConfigData('Details', 'Browser'))=="chrome"):
        path = "./Driver/chromedriver.exe"
        driver=Chrome(executable_path=path)
    elif((configReader.readConfigData('Details', 'Browser'))=="firefox"):
        path = "./Driver/geckodriver.exe"
        driver = Chrome(executable_path=path)
    else:
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    driver.get(configReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
