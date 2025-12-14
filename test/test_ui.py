import pytest
from selenium import webdriver
import allure
from UIPage import SearchPage
from time import sleep

@pytest.fixture(scope=session)
def driver():
    driver = webdriver.chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def search_page(driver):
    page = SearchPage(driver)
    page.open("https://www.chitai-gorod.ru/")
    sleep(5)
    return page

def test_search_book_by_title():
    with allure.step("Ввести запрос на поиск книги по названию"):
        search_page.enter_search_query("Капитанская дочка")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("Капитанская дочка" in title for title in product_titles), "Название книги не найдено в списке книг"