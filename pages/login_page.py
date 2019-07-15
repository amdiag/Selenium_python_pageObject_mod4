# from pages import locators
from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators
from .login_page import LoginPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url()
        assert current_link.__contains__("login"), "Login link is not presented. Current - " + current_link

    def should_be_login_form(self):
        assert self.is_element_presence(*LoginPageLocators.LOGIN_FORM_LINK), "Login form link isn't exist"

    def should_be_register_form(self):
        assert self.is_element_presence(*LoginPageLocators.REGISTER_FORM_LINK), "Register form link isn't exist"
