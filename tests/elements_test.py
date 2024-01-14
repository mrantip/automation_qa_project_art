import random
import time

import allure

from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:

    @allure.feature('TextBox Page')
    class TestTextBoxPage:

        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'full name does not match'
            assert email == output_email, 'email does not match'
            assert current_address == output_cur_addr, 'fcurrent_address does not match'
            assert permanent_address == output_per_addr, 'permanent_address does not match'

    @allure.feature('CheckBox Page')
    class TestCheckBoxPage:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    @allure.feature('RadioButton Page')
    class TestRadioButtonPage:

        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    @allure.feature('WebTable Page')
    class TestWebTablePage:

        @allure.title('Check adding a person to the table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        @allure.title('Check search of a person in the table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, " the person was not found in the table"

        @allure.title('Check the updating a person in the table')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            time.sleep(5)
            age = web_table_page.update_person_info()
            time.sleep(5)
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @allure.title('Check the removing a person from the table')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "The number of rows in the table has not been changed or has changed incorrect"

    @allure.feature('Button Page')
    class TestButtonPage:

        @allure.title('Check the clicking on the buttons different types')
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

        @allure.title('Check the clicking on the double-click button')
        def test_double_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_double_click_button()
            assert double == "You have done a double click", "The double click button was not pressed"

        @allure.title('Check the clicking on the right-click button')
        def test_right_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            right = button_page.click_on_right_click_button()
            assert right == "You have done a right click", "The right click button was not pressed"

        @allure.title('Check the clicking on the dynamic-click button')
        def test_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            click = button_page.click_on_click_button()
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

    @allure.feature('Links Page')
    class TestLinksPage:

        @allure.title('Check the link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'The link is broken or url is incorrect'

        @allure.title('Check the dynamic link')
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url, 'The link is broken or url is incorrect'

        @allure.title('Check the broken link')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'The link works or the status code is not 400'

        @allure.title('Check all-api link')
        def test_all_api_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code_created = links_page.check_created_link('https://demoqa.com/created')
            response_code_no_content = links_page.check_no_content_link('https://demoqa.com/no-content')
            response_code_moved = links_page.check_moved_link('https://demoqa.com/moved')
            response_code_bad_request = links_page.check_broken_link('https://demoqa.com/bad-request')
            response_code_unauthorized = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
            response_code_forbidden = links_page.check_forbidden_link('https://demoqa.com/forbidden')
            response_code_not_found = links_page.check_not_found_link('https://demoqa.com/invalid-url')
            assert response_code_created == 201, 'The link works or the status code is not 201'
            assert response_code_no_content == 204, 'The link works or the status code is not 204'
            assert response_code_moved == 301, 'The link works or the status code is not 301'
            assert response_code_bad_request == 400, 'The link works or the status code is not 400'
            assert response_code_unauthorized == 401, 'The link works or the status code is not 401'
            assert response_code_forbidden == 403, 'The link works or the status code is not 403'
            assert response_code_not_found == 404, 'The link works or the status code is not 404'

    @allure.feature('Upload And Download Page')
    class TestUploadAndDownloadPage:

        @allure.title('Check upload a file')
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'

        @allure.title('Check download a file')
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, 'The file has not been downloaded'

    @allure.feature('Dynamic Properties Page')
    class TestDynamicPropertiesPage:

        @allure.title('Check the enable button')
        def test_enable_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            enable = dynamic_properties.check_enable_button()
            assert enable is True, 'button has not been enabled'

        @allure.title('Check the dynamic properties')
        def test_dynamic_properties(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            color_before, color_after = dynamic_properties.check_changed_of_color()
            assert color_before != color_after, 'colors have not been changed'

        @allure.title('Check the appear button')
        def test_appear_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            appear = dynamic_properties.check_appear_of_button()
            assert appear is True, 'button has not been appeared'
