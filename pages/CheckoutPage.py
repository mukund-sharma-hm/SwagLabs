
from pages.BasePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    
    checkout_button_xpath = "//a[@class='btn_action checkout_button']"
    your_information_xpath="//div[@class='subheader']"
    first_name_id="first-name"
    last_name_id="last-name"
    zip_code_id="postal-code"
    continue_button_xpath="//input[@class='btn_primary cart_button']"
    information_assert_xpath="//button[@class='error-button']"
    cancel_button_xpath="//a[@class='cart_cancel_link btn_secondary']"
    your_cart_assert_xpath="//div[@class='subheader']"
    def checkout_btn(self):
        return self.click_element("checkout_button_xpath",self.checkout_button_xpath)
    def your_information(self):
        return self.check_display_status_of_element("your_information_xpath",self.your_information_xpath)
    def enter_first_name(self, first_name):
        self.type_into_element(first_name, "first_name_id", self.first_name_id)
    def enter_last_name(self, last_name):
        self.type_into_element(last_name, "last_name_id", self.last_name_id)
    def enter_zip_code(self, zip_cde):
        self.type_into_element(zip_cde, "zip_code_id", self.zip_code_id)
    def continue_btn(self):
        return self.click_element("continue_button_xpath",self.continue_button_xpath)
    def details_is_required_assert(self):
        return self.check_display_status_of_element("information_assert_xpath",self.information_assert_xpath)
    def cancel_btn(self):
        return self.click_element("cancel_button_xpath",self.cancel_button_xpath)
    def your_cart(self):
        return self.check_display_status_of_element("your_cart_assert_xpath",self.your_cart_assert_xpath
                                                    )
