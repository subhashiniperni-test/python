from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
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
    #working on name
    driver.find_element_by_name("fld_username").send_keys("Subhashini")

    #working on email
    driver.find_element_by_name("fld_email").send_keys("subhashini17@gmail.com")

    #working on password
    driver.find_element_by_name("fld_password").send_keys("123456")

    # working on confrim password
    driver.find_element_by_name("fld_cpassword").send_keys("123456")

    # working on date of birth
    driver.find_element_by_name("dob").send_keys("18/12/1988")

    # working on phone
    driver.find_element_by_name("phone").send_keys("1234567890")

    #work on drop down
    obj = Select(driver.find_element_by_name("sex"))
    obj.select_by_visible_text("Male")
    #time.sleep(20)
    #working on radio button
    driver.find_element_by_xpath("//input[@value='home']").click()

    #working on check box
    driver.find_element_by_name("terms").click()

    #working on Button
    driver.find_element_by_xpath("//input[@type='submit']").click()

    #working on Links
    driver.find_element_by_link_text("Read Detail").click()
    #time.sleep(2)