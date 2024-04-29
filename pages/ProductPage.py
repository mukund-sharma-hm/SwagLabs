from pages.BasePage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_page_title_xpath = "//div[@id='inventory_filter_container']/div"
    product_on_page_xpath = "//*[@id='inventory_container']"
    add_to_cart_button_xpath = "//div[@id='inventory_container']//button"
    verify_cart_product_xpath = "//*[@id='item_4_title_link']/div"
    cart_icon_xpath = "//div[@id='shopping_cart_container']"
    dropdown_filter_xpath = "//*[@id='inventory_filter_container']/select"
    dropdown_filter_option_xpath = "./option"

    def display_status_of_page(self):
        return self.check_display_status_of_element("valid_page_title_xpath", self.valid_page_title_xpath)

    def display_product_of_page(self):
        return self.check_display_status_of_element("product_on_page_xpath", self.product_on_page_xpath)

    def add_to_cart_button(self):
        return self.click_element("add_to_cart_button_xpath", self.add_to_cart_button_xpath)

    def cart_icon(self):
        return self.click_element("cart_icon_xpath", self.cart_icon_xpath)

    def match_the_product_name(self):
        return self.retrieve_message_text("verify_cart_product_xpath", self.verify_cart_product_xpath)

