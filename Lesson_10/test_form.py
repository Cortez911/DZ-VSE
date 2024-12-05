import allure
import pytest
from selenium import webdriver
from form_page import FormPage


@allure.title("Тест заполнения формы")
@allure.description("Проверяет заполнение всех полей формы и валидацию.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form(browser: webdriver.Chrome):
    form_page = FormPage(browser)
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html") # Добавлена строка для перехода на нужную страницу
    with allure.step("Заполнение формы"):
        form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    with allure.step("Проверка элементов формы"):
        assert form_page.get_zip_code_element().get_attribute("class") == "alert py-2 alert-danger"
        assert form_page.get_first_name_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_last_name_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_address_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_city_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_country_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_email_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_phone_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_job_position_element().get_attribute("class") == "alert py-2 alert-success"
        assert form_page.get_company_element().get_attribute("class") == "alert py-2 alert-success"
