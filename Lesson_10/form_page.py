from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех Page Objects."""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


class FormPage(BasePage):
    """Page Object для страницы с формой."""
    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, city: str, country: str, job_position: str, company: str) -> None:
        """Заполняет форму."""
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input").send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, "div.col-md-4.py-2 > button").click()

    def get_element(self, locator: tuple) -> webdriver.remote.webelement.WebElement:
        """Возвращает WebElement по локатору, используя явное ожидание."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_zip_code_element(self) -> webdriver.remote.webelement.WebElement:
        """Возвращает WebElement для поля 'zip-code'."""
        return self.get_element((By.ID, "zip-code"))

    def get_first_name_element(self) -> webdriver.remote.webelement.WebElement:
        """Возвращает WebElement для поля 'first-name'."""
        return self.get_element((By.CSS_SELECTOR, "#first-name"))

    def get_last_name_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#last-name"))

    def get_address_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#address"))

    def get_city_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#city"))

    def get_country_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#country"))

    def get_email_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#e-mail"))

    def get_phone_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#phone"))

    def get_job_position_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#job-position"))

    def get_company_element(self) -> webdriver.remote.webelement.WebElement:
        return self.get_element((By.CSS_SELECTOR, "#company"))
