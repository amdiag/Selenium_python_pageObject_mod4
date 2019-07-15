from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_link')
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators(object):
    BTN_ADD_TO_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    # BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BASKET_COST = (
    By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
