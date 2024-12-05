from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    """Базовый класс для всех Page Objects."""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


class LoginPage(BasePage):
    """Page Object для страницы логина."""
    def login(self, username: str, password: str) -> None:
        """Выполняет логин."""
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)


class ProductsPage(BasePage):
    """Page Object для страницы продуктов."""
    def add_to_cart(self, product_id: str) -> None:
        """Добавляет товар в корзину."""
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_id}")))
        add_button.click()

    def go_to_cart(self) -> None:
        """Переходит к корзине."""
        shopping_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()


class CartPage(BasePage):
    """Page Object для страницы корзины."""
    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()


class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа."""
    def fill_form(self, firstname: str, lastname: str, zipcode: str) -> None:
        """Заполняет форму."""
        firstname_field = self.driver.find_element(By.ID, "first-name")
        firstname_field.send_keys(firstname)
        lastname_field = self.driver.find_element(By.ID, "last-name")
        lastname_field.send_keys(lastname)
        zipcode_field = self.driver.find_element(By.ID, "postal-code")
        zipcode_field.send_keys(zipcode)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму."""
        total_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total_element.text[7:]
