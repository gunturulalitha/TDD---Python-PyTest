''' Parallel Execution '''

from selenium import webdriver
import pytest

driver = None

@pytest.fixture(scope = 'module')
def driver_initialization():
    global driver
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(3)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    yield
    driver.quit()

@pytest.mark.usefixtures("driver_initialization")
def test_google_title():
    print("Google Title")
    assert driver.title == "Google"

@pytest.mark.usefixtures("driver_initialization")
def test_google_url():
    print("Current URL")
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"


