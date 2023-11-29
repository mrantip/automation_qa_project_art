from pages.base_page import BasePage


def test_1(driver):
    page = BasePage(driver, 'https://www.google.com/')
    page.open()
