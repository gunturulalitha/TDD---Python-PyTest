from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def init_chrome_driver():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    #requests.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures('init_chrome_driver')
class Base_chrome_test:
    pass

class Test_google_chrome(Base_chrome_test):
    def test_google(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


