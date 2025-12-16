import requests
import allure

class ApiPage:

   def __init__(self, base_url, token):
       self.base_url = base_url
       self.token = token

   def _get_headers(self):
       return {"Content-type": "application/json",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",

                "Authorization": f"Bearer {self.token}"}



   @allure.step("Поиск продукта по фразе: {phrase}")
   def search_product(self, phrase, customer_city_id = 54):
       params = {"customerCityId": customer_city_id,
                 "phrase": phrase}
       response = requests.get(self.base_url, headers=self._get_headers(), params=params)
       allure.attach(response.text, "Ответ API")
       return response

   @allure.step("Извлечение названий книг из ответа")
   def exstract_book_titles(self, response_json):
       titles = [book['attributes']['title'] for book in response_json.get(
           'included', []) if book['type'] == 'product']
       allure.attach(str(titles), "Названия книг")
       return titles