import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_tab()
        text_title = self.element_is_present(self.locators.TITLE_NEW_BUTTON).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_tab()
        text_title = self.element_is_present(self.locators.TITLE_NEW_BUTTON).text
        return text_title
