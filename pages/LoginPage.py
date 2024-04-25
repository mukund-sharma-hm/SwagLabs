from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    username_field_id = "user-name"
    password_field_id = "password"
    login_button_id = "login-button"
    warning_message_xpath = "//div[@id='login_button_container']/div/form/h3"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username_into_username_field(self, user_name):
        self.type_into_element(user_name, "username_field_id", self.username_field_id)

    def enter_password_into_password_field(self, pass_word):
        self.type_into_element(pass_word, "password_field_id", self.password_field_id)

    def click_on_the_login_button(self):
        self.click_element("login_button_id", self.login_button_id)

    def retrieve_warning_message(self):
        return self.retrieve_message_text("warning_message_xpath", self.warning_message_xpath)

    def login_to_homepage(self, user_name, pass_word):
        self.enter_username_into_username_field(user_name)
        self.enter_password_into_password_field(pass_word)
        self.click_on_the_login_button()
