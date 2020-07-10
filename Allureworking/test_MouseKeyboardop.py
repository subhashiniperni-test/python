from datetime import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path="C:/Users/subhashinip/Downloads/chromedriver_win32/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("http://www.theTestingworld.com")
    driver.maximize_window()

def test_mouse_keyboard(environment_setup):
    #mouse operations
    act = ActionChains(driver)
    act.click().perform()
    act.context_click().perform()
    act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
    #act.double_click().perform()
    act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #act.move_to_element(driver.find_element_by_xpath("//span[contains(text()='TUTORIAL']")).perform()
