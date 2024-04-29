from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_page_title_xpath = "//div[@id='inventory_filter_container']/div"
    product_on_page_xpath = "//*[@id='inventory_container']"
    add_to_cart_button_xpath = "//div[@id='inventory_container']//button"
    verify_cart_product_xpath = "//*[@id='item_4_title_link']/div"
    cart_button_xpath = "//div[@id='shopping_cart_container']"
    verify_cart_button_xpath = "//div[@class='subheader']"
    dropdown_filter_xpath = "//*[@id='inventory_filter_container']/select"
    product_list_xpath = "//div[@class='inventory_item_name']"
    product_price_xpath = "//div[@class='inventory_item_price']"

    def display_status_of_page(self):
        return self.check_display_status_of_element("valid_page_title_xpath", self.valid_page_title_xpath)

    def display_product_of_page(self):
        return self.check_display_status_of_element("product_on_page_xpath", self.product_on_page_xpath)

    def add_to_cart_button(self):
        return self.click_element("add_to_cart_button_xpath", self.add_to_cart_button_xpath)

    def cart_button(self):
        return self.click_element("cart_button_xpath", self.cart_button_xpath)

    def cart_button_text(self):
        return self.retrieve_message_text("verify_cart_button_xpath", self.verify_cart_button_xpath)

    def match_the_product_name(self):
        return self.retrieve_message_text("verify_cart_product_xpath", self.verify_cart_product_xpath)

    def dropdown_filter(self, index):
        return self.select_option("dropdown_filter_xpath", self.dropdown_filter_xpath, index)

    def sort_product_list_name(self):
        return self.get_elements("product_list_xpath",self.product_list_xpath)

    def sort_product_list_price(self):
        return self.get_elements("product_price_xpath", self.product_price_xpath)






