import allure
import pytest
from selenium import webdriver
from e_commerce_pages import LoginPage, ProductsPage, CartPage, CheckoutPage


@allure.title("Тест авторизации и оформления заказа")
@allure.description("Проверяет весь процесс: авторизацию, добавление товаров в корзину и оформление заказа.")
@allure.feature("E-commerce")
@allure.severity(allure.severity_level.BLOCKER)
def test_e_commerce(browser: webdriver.Chrome):
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    with allure.step("Авторизация"):
        login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser)
    with allure.step("Добавление товаров в корзину"):
        products_page.add_to_cart("sauce-labs-backpack")
        products_page.add_to_cart("sauce-labs-bolt-t-shirt")
        products_page.add_to_cart("sauce-labs-onesie")
    with allure.step("Переход к корзине"):
        products_page.go_to_cart()

    cart_page = CartPage(browser)
    with allure.step("Переход к оформлению заказа"):
        cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    with allure.step("Заполнение формы"):
        checkout_page.fill_form("Тест", "Тестович", "010101")
    with allure.step("Проверка итоговой стоимости"):
        total = checkout_page.get_total()
        assert total == "$58.29"