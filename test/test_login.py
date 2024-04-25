import pytest
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from test.BaseTest import BaseTest


class TestLogin(BaseTest):
    def test_login_for_a_valid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        assert product_page.display_status_of_page()

    def test_login_for_a_invalid_username_and_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("stand_user", "secret_sauce")
        expected_warning_text = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.retrieve_warning_message().__eq__(expected_warning_text)

    def test_login_for_a_valid_username_and_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "sect_sauce")
        expected_warning_text = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.retrieve_warning_message().__eq__(expected_warning_text)

    def test_login_for_a_invalid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("stand_user", "sect_sauce")
        expected_warning_text = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.retrieve_warning_message().__eq__(expected_warning_text)
