from pages.LoginPage import LoginPage
from test.BaseTest import BaseTest
from pages.ProductPage import ProductPage
from pages.LogoutPage import LogoutPage


class TestLogout(BaseTest):


    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_homepage("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)
        assert product_page.display_status_of_page()

        logout_page = LogoutPage(self.driver)
        logout_page.left_side_bar()
        logout_page.loading_time()
        logout_page.logout_button_click()

        assert logout_page.expected_url_value() in logout_page.check_current_url()
