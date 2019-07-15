from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_link')
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators(object):
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '#btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '#')
    BASKET_COST = (By.CSS_SELECTOR, '#')
