import pytest
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from test.BaseTest import BaseTest


class TestLoginErrorMessage(BaseTest):
    def test_login_for_a_blank_credential(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("","")
        expected_test = "Epic sadface: Username is required"
        assert login_page.retrieve_warning_message().__eq__(expected_test)

    def test_login_for_a_blank_username_and_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("", "secret_sauce")
        expected_test = "Epic sadface: Username is required"
        assert login_page.retrieve_warning_message().__eq__(expected_test)

    def test_login_for_a_valid_username_and_blank_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "")
        expected_test = "Epic sadface: Password is required"
        assert login_page.retrieve_warning_message().__eq__(expected_test)

    def test_login_for_a_invalid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("stand_user", "sect_sauce")
        expected_test = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.retrieve_warning_message().__eq__(expected_test)
