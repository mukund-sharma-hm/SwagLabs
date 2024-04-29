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
        product_page.cart_button()

        expected_text = "Sauce Labs Backpack"
        assert product_page.match_the_product_name().__eq__(expected_text)

    def test_cart_button(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user","secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.cart_button()

        expected_text = "Your Cart"
        assert product_page.cart_button_text().__eq__(expected_text)

    def test_sort_button_name_a_to_z(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user","secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.dropdown_filter(0)

        product_list = product_page.sort_product_list_name()
        for i in range(len(product_list) - 1):
            assert product_list[i].text <= product_list[i + 1].text

    def test_sort_button_name_z_to_a(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user","secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.dropdown_filter(1)

        product_list = product_page.sort_product_list_name()
        for i in range(len(product_list) - 1):
            assert product_list[i].text >= product_list[i + 1].text

    def test_sort_button_price_low_to_high(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.dropdown_filter(2)

        product_list = product_page.sort_product_list_price()
        prices = [float(product.text.replace('$', '')) for product in product_list]
        is_sorted = all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
        assert is_sorted

    def test_sort_button_price_high_to_low(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        product_page.dropdown_filter(3)

        product_list = product_page.sort_product_list_price()
        prices = [float(product.text.replace('$', '')) for product in product_list]
        is_sorted = all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1))
        assert is_sorted



