from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    time.sleep(5)
    page.solve_quiz_and_get_code()
    time.sleep(5)
    # page.check_product_in_basket("")
    # page.check_cost_of_basket()
