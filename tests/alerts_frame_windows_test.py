import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindowsPage:

        @allure.title('Check the opening of a new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'The new tab has not been opened or an incorrect tab has been opened'

        @allure.title('Check the opening of a new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'The window tab has not been opened or an incorrect window has been opened'

    @allure.feature('Alerts Page')
    class TestAlertsPage:

        @allure.title('Check the opening of an alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Check the opening of the alert after 5 seconds')
        def test_see_alert_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        @allure.title('Check the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'Alert did not show up'

        @allure.title('Check the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert alert_text == f'You entered {text}', 'Alert did not show up'

    @allure.feature('Frame Page')
    class TestFramePage:

        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['500px', '350px', 'This is a sample page'], 'The frame does not exist'
            assert result_frame2 == ['100px', '100px', 'This is a sample page'], 'The frame does not exist'

    @allure.feature('Nested Frames Page')
    class TestNestedFramesPage:

        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialogs Page')
    class TestModalDialogsPage:

        @allure.title('Check the page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1], 'text from large dialog is less than text from small dialog'
            assert small[0] == 'Small Modal', 'The header is not "Small Modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large Modal"'

        @allure.title('Check the page with small modal dialogs')
        def test_small_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small = modal_dialogs_page.check_small_modal_dialogs()
            assert small == 'Small Modal', 'The header is not "Small Modal"'

        @allure.title('Check the page with large modal dialogs')
        def test_large_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            large = modal_dialogs_page.check_large_modal_dialogs()
            assert large == 'Large Modal', 'The header is not "Large Modal"'
