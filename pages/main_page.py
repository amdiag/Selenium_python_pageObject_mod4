import selenium.webdriver.common.by

from .base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "#login_link")
        link.click()
