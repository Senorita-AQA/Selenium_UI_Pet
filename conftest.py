import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def auth_user(browser):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.login_btn()
    yield browser
    browser.quit()



