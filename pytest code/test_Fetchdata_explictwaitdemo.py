from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
    driver = Chrome(executable_path=path)
   # driver.set_page_load_timeout(1)
    driver.get("http://www.thetestingworld.com/testings")
   # driver.implicitly_wait(10)
    driver.maximize_window()

    yield
    driver.close()

def test_registration_valid_data(environment_setup):
    wait = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))

    #working on select
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID,'stateId'),"Andhra Pradesh"))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Andhra Pradesh")



