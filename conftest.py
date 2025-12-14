import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    def driver():
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return browser
        yield browser
        browser.quit()