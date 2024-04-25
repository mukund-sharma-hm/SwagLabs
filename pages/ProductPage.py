from pages.BasePage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_page_title_xpath = "//div[@id='inventory_filter_container']/div"

    def display_status_of_page(self):
        return self.check_display_status_of_element("valid_page_title_xpath", self.valid_page_title_xpath)

