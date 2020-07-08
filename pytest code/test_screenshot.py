from selenium.webdriver import Chrome


def test_screenshot():
    path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("http://www.thetestingworld.com/testings")
    take_screenshot(driver,"AF")


def take_screenshot(driver,name):
    driver.get_screenshot_as_file("C:/Users/Subhashini/PycharmProjects/python/pytest code/" + name +".png")
