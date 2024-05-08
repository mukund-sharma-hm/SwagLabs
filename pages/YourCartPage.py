from pages.BasePage import BasePage


class YourCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    remove_xpath="//button[@class='btn_secondary cart_button']"
    continue_xpath="//a[@class='btn_secondary']"
    description_xpath="//div[@class='inventory_item_desc']"

    def remove_button(self):
        return self.click_element("remove_xpath",self.remove_xpath)

    def continue_button(self):
        return self.click_element("continue_xpath",self.continue_xpath)

    def description_text(self):
        return self.retrieve_message_text("description_xpath", self.description_xpath)
