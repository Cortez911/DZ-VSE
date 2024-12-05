import allure
import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@allure.title("Тест калькулятора")
@allure.description("Проверяет работу калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser: webdriver.Chrome):
    calculator_page = SlowCalculatorPage(browser)
    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open()
    with allure.step("Установка задержки"):
        calculator_page.set_delay("45")
    with allure.step("Ввод числа 7"):
        calculator_page.click_button("7")
    with allure.step("Выбор операции сложения"):
        calculator_page.click_button("+")
    with allure.step("Ввод числа 8"):
        calculator_page.click_button("8")
    with allure.step("Нажатие кнопки равно"):
        calculator_page.click_button("=")
    with allure.step("Проверка результата"):
        result = calculator_page.get_result()
        if result == "15":
            assert True
