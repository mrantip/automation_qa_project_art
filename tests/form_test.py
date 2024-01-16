import time

import allure

from pages.form_page import FormPage


@allure.suite('Form')
class TestForm:
    @allure.feature('Form Page')
    class TestFormPage:

        @allure.title('Check form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [person_info.firstname + ' ' + person_info.lastname, person_info.email] == [result[0], result[
                1]], 'The form has not been filled'
