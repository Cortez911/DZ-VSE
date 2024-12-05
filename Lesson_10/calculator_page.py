from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=0.5, ignored_exceptions=[StaleElementReferenceException])


class SlowCalculatorPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_field_locator = (By.CSS_SELECTOR, "#delay")
        self.button_locators = {
            '7': (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)"),
            '+': (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)"),
            '8': (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)"),
            '=': (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning"),
            'C': (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-secondary")
        }
        self.result_locator = (By.XPATH, "//div[@id='calculator']//div[@class='top']//div[@class='screen']")

    def open(self) -> None:
        self.driver.get(self.url)

    def set_delay(self, value: str) -> None:
        try:
            delay_field = self.wait.until(EC.presence_of_element_located(self.delay_field_locator))
            delay_field.clear()
            delay_field.send_keys(value)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка установки задержки: {e}")
            raise

    def click_button(self, button_text: str) -> None:
        locator = self.button_locators.get(button_text)
        if locator is None:
            raise ValueError(f"Кнопка '{button_text}' не найдена.")
        try:
            button = self.wait.until(EC.element_to_be_clickable(locator))
            button.click()
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Ошибка нажатия кнопки '{button_text}': {e}")
            raise

    def get_result(self) -> str:
        try:
            result_element = self.wait.until(EC.presence_of_element_located(self.result_locator))
            # Ожидаем, пока текст элемента станет непустым И изменится
            self.wait.until(lambda driver: result_element.text.strip() and result_element.text.strip() != "7+8") #пример для 7+8
            return result_element.text.strip()
        except (TimeoutException, NoSuchElementException) as e:
            return f"Ошибка получения результата: {e}"
