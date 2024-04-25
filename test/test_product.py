from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from test.BaseTest import BaseTest


class TestLogin(BaseTest):
    def test_login_for_a_valid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        assert product_page.display_status_of_page()

    def test_add_to_cart_button(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.add_to_cart_button()
        product_page.cart_icon()

        expected_text = "Sauce Labs Backpack"
        assert product_page.match_the_product_name().__eq__(expected_text)
