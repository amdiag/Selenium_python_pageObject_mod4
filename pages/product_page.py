from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def check_product_in_basket(self, product_name):
        print("product_name")

    def check_cost_of_basket(self):
        print("")
