from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import chromeDriverManager

from page.AuthPage import AuthPage

def first_test():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicity_wait(4)
    browser.maximize_window()

    auth_page = AuthPage(browser)
    auth_page.go()