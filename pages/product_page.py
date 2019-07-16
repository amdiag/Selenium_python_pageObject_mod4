from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_button_add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def check_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_site = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        # print("site - {}. product - {}".format(product_name.text, name_site.text))
        assert name_site.text == product_name.text, "Unknown product or unexist. Current: \'{}\'".format(name_site.text)

    def check_cost_of_basket(self):
        cost_basket_site = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        # print("site - {}. product - {}".format(cost_basket_site.text, product_cost.text))
        assert product_cost.text == cost_basket_site.text, "Unknown price. Current: \'{}\'".format(
            cost_basket_site.text)

    def check_success_add_to_basket(self):
        alertinner_text = self.browser.find_elements_by_class_name("alertinner")[0].text
        assert alertinner_text == "{} has been added to your basket.".format(
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text), "Error adding to basket"
