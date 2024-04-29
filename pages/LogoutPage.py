from pages.BasePage import BasePage

class LogoutPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    corner_bar_xpath = '//div[@class="bm-burger-button"]/button'
    logout_button_id = "logout_sidebar_link"
    expected_url = "https://www.saucedemo.com/v1/"
    
    def left_side_bar(self):
        return self.click_element("corner_bar_xpath",self.corner_bar_xpath)
    
    def logout_button_click(self):
        return self.click_element("logout_button_id",self.logout_button_id)
    
    def expected_url_value(self):
        return self.expected_url
    
    def check_current_url(self):
        return self.driver.current_url
    
    def loading_time(self):
        return self.driver.implicitly_wait(3)