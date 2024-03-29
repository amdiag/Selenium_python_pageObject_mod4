from pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
