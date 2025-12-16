import pytest
from selenium import webdriver
import selenium
import allure
from final_proj.page.UiPage import SearchPage


from time import sleep

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def search_page(driver):
    page = SearchPage(driver)
    page.open("https://www.chitai-gorod.ru/")
    sleep(5)
    return page

def test_search_book_by_title(search_page):
    with allure.step("Ввести запрос на поиск книги по названию"):
        search_page.enter_search_query("Капитанская дочка")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("Капитанская дочка" in title for title in product_titles), "Название книги не найдено в списке книг"

def test_search_book_by_author(search_page):
    with allure.step("Ввести запрос на поиск книги по имени автора"):
        search_page.enter_search_query("Пушкин")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("Пушкин" in title for title in product_titles), "Название книги не найдено в списке книг"

def test_search_book_by_arabian(search_page):
    with allure.step("Ввести запрос на поиск книги по названию на арабском языке"):
        search_page.enter_search_query("بوشكين")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("بوشكين" in title for title in product_titles), "Название книги не найдено в списке книг"

def test_search_book_by_english(search_page):
    with allure.step("Ввести запрос на поиск книги по названию на арабском языке"):
        search_page.enter_search_query("Pushkin")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("Pushkin" in title for title in product_titles), "Название книги не найдено в списке книг"

def test_search_book_by_korean(search_page):
    with allure.step("Ввести запрос на поиск книги по названию на корейском языке"):
        search_page.enter_search_query("푸시킨")
        sleep(5)
    with allure.step("Нажать кнопку поиска"):
        search_page.click_search_button()
    with allure.step("Получить заголовки книг"):
        product_titles = search_page.get_product_titles()
    assert any ("푸시킨" in title for title in product_titles), "Название книги не найдено в списке книг"