from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def setPath(scope="module"):
    global driver
    path = "C:/DdriveData/downloads/chromedriver_win32/chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

def test_registration_valid_data(setPath):
    driver.get("http://www.thetestingworld.com")
    driver.maximize_window()
    assert driver.current_url == "http://www.thetestingworld.com"

def test_registration_invalid_data(setPath):
    driver.get("http://www.google.com")
    driver.maximize_window()
    assert driver.current_url == "http://www.thegoogle.com"

def test_invalid_data(setPath):
    driver.get("http://www.thetestingworld.com")
    driver.maximize_window()
    assert driver.current_url == "http://www.testingworld.com"


