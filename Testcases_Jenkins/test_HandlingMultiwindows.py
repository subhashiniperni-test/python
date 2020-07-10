from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

def test_multiwindow(environment_setup):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys("test")
    driver.find_element_by_name("_txtPassword").send_keys("test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
    driver.find_element_by_xpath("//a[contains(text() , 'My Account')]").click()
    driver.find_element_by_xpath("//a[contains(text() , 'Update')]").click()
    allwin = driver.window_handles
    Mainwin = ""
    for win in allwin:
        driver.switch_to.window(win)
        #print(driver.current_url)
        if(driver.current_url=="https://www.thetestingworld.com/testings/manage_customer.php"):
          #  driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif(driver.current_url=="https://www.thetestingworld.com/testings/dashboard.php"):
            Mainwin=win

    driver.switch_to.window(Mainwin)
    print(driver.current_url)



