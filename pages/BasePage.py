from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_message_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def select_option(self, locator_name, locator_value, index):
        dropdown = self.get_element(locator_name, locator_value)
        return Select(dropdown).select_by_index(index)

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_elements(self, locator_name, locator_value):
        elements = None
        if locator_name.__contains__("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_name.__contains__("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_name.__contains__("_class_name"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_name.__contains__("_css"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        return elements

