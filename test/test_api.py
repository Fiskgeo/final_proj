import allure
from ApiPage import ApiPage

 base_url = "https://www.chitai-gorod.ru/search?phrase"
 token = "Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjYxMTksImlhdCI6MTc2NTY5MDA5NywiZXhwIjoxNzY1NjkzNjk3LCJ0eXBlIjoyMCwianRpIjoiMDE5YjFiNTQtYzE0Zi03N2VlLWJjYWUtNTc0ZWRiYzc1MTBkIiwicm9sZXMiOjEwfQ.HZw6hhOhLAbREV9pg3eP2L8nQ_XfKdhF0EixH4vlog4"

#Инициализация объекта API
 api_page = ApiPage(base_url, token)

 @allure.epic("API тестирование сайта Читай-город")
 @allure.feature("Поиск книг")
 @allure.title("Поиск книги по названию")
 @allure.description("Проверка что API возвращает книгу с ожидаемым названием")

 def test_api_book_by_title():
     responce = api_page.search_product("Капитанская дочка")
     #Вывод текста ответа и статус кода для отладки
     print("Ответ:", responce.text)
     print("Статус код:", responce.status_code)
     #Проверка статуса ответа
     assert responce.status_code == 200, f"Тест провален, статус-код {responce.status_code}."

     expected_title = "Капитанская дочка"
     responce_json = responce.json()
     book_titles = api_page.exstract_book_titles(responce_json)
     assert any (expected_title.lower() in title.lower() for title in book_titles)
     f"Тест провален: название книги '{expected_title}' не найдено в ответе"


def test_api_book_by_author():
    responce = api_page.search_product("Пушкин")
    # Вывод текста ответа и статус кода для отладки
    print("Ответ:", responce.text)
    print("Статус код:", responce.status_code)
    # Проверка статуса ответа
    assert responce.status_code == 200, f"Тест провален, статус-код {responce.status_code}."

    expected_title = "Пушкин"
    responce_json = responce.json()
    book_titles = api_page.exstract_book_titles(responce_json)
    assert any(expected_title.lower() in title.lower() for title in book_titles)
    f"Тест провален: название книги '{expected_title}' не найдено в ответе"

def test_api_book_by_arabian():
    responce = api_page.search_product("بوشكين")
    # Вывод текста ответа и статус кода для отладки
    print("Ответ:", responce.text)
    print("Статус код:", responce.status_code)
    # Проверка статуса ответа
    assert responce.status_code == 200, f"Тест провален, статус-код {responce.status_code}."

    expected_title = "بوشكين"
    responce_json = responce.json()
    book_titles = api_page.exstract_book_titles(responce_json)
    assert any(expected_title.lower() in title.lower() for title in book_titles)
    f"Тест провален: название книги '{expected_title}' не найдено в ответе"

def test_api_book_by_english():
    responce = api_page.search_product("Pushkin")
    # Вывод текста ответа и статус кода для отладки
    print("Ответ:", responce.text)
    print("Статус код:", responce.status_code)
    # Проверка статуса ответа
    assert responce.status_code == 200, f"Тест провален, статус-код {responce.status_code}."

    expected_title = "Pushkin"
    responce_json = responce.json()
    book_titles = api_page.exstract_book_titles(responce_json)
    assert any(expected_title.lower() in title.lower() for title in book_titles)
    f"Тест провален: название книги '{expected_title}' не найдено в ответе"

def test_api_book_by_korean():
    responce = api_page.search_product("푸시킨")
    # Вывод текста ответа и статус кода для отладки
    print("Ответ:", responce.text)
    print("Статус код:", responce.status_code)
    # Проверка статуса ответа
    assert responce.status_code == 200, f"Тест провален, статус-код {responce.status_code}."

    expected_title = "푸시킨"
    responce_json = responce.json()
    book_titles = api_page.exstract_book_titles(responce_json)
    assert any(expected_title.lower() in title.lower() for title in book_titles)
    f"Тест провален: название книги '{expected_title}' не найдено в ответе"
