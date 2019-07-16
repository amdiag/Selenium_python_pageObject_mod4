from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def check_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_site = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert name_site.text == product_name, "Unknown product or unexist. Current: \'{}\'".format(name_site.text)

    def check_cost_of_basket(self):
        print("")
        # cost_basket_site = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        # product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        # assert product_cost == cost_basket_site.text, "Unknown price. Current: \'{}\'".format(cost_basket_site.text)
        # ToDO change path for product cost, get from site and compare it

    def check_success_add_to_basket(self):
        print("")
        # ToDO imlement me ///The shellcoder's handbook has been added to your basket.
