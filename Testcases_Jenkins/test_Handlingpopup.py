import selenium.webdriver

def test_handlingpopup():

    path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
    driver = selenium.webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    mainwin=""
    driver.get("https://www.naukri.com")
    Allwindow = driver.window_handles

    for win in Allwindow:
        driver.switch_to.window(win)
        if(driver.current_url == "https://www.naukri.com/"):
            mainwin=win
        else:
            driver.close()
    driver.switch_to.window(mainwin)
    print(driver.current_url)


