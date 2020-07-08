import selenium.webdriver

path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
driver = selenium.webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.thetestingworld.com/testings")
driver.execute_script("window.scrollTo(0,400);")
