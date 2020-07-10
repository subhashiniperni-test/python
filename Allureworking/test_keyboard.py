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

def test_keyboard(environment_setup):
    #keyboard operations
     driver.find_element_by_name("fld_username").send_keys("abcdhello")
     act = ActionChains(driver)
     act.send_keys(Keys.TAB).perform()
    #act.key_down(Keys.CONTROL).send_keys('a').perform()
    #time.sleep(10)
    #act.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.DELETE).perform()
