from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

def test_openpage():
    path="C:/Users/subhashinip/Downloads/chromedriver_win32/chromedriver.exe"
    driver=Chrome(executable_path=path)

    driver.get("http://www.theTestingworld.com/testings")
    driver.maximize_window()

    driver.find_element_by_name("fld_username").send_keys("Helloworld")
    driver.find_element_by_name("fld_email").send_keys("abcd@xyz.com")
    driver.find_element_by_name("fld_password").send_keys("abcde")
    driver.find_element_by_name("fld_cpassword").send_keys("abcde")
    #driver.find_element_by_name("fld_username").clear()
    #driver.find_element_by_name("fld_username").send_keys("HiABCD")
    driver.find_element_by_xpath("//input[@value='home']").click()

    obj= Select(driver.find_element_by_name("sex"))
    #obj.select_by_value("2")
    #obj.select_by_index(1)
    obj.select_by_visible_text("Male")






#driver.find_element_by_name("terms").click()
#driver.find_element_by_xpath("//input[@value='Sign up']").click()
#driver.find_element_by_link_text("Read Detail").click()
#driver.close()
