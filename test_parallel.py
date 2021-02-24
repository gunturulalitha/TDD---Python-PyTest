''' Parallel Execution '''

from selenium import webdriver


def test_google():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://www.google.com")
    assert driver.title == "Google"

def test_facebook():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook - Log In or Sign Up"

def test_gmail():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://www.gmail.com")
    assert driver.title == "Gmail"

def test_instagram():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

