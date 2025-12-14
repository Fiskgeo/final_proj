import requests
import allure

class ApiPage:

   def __init__(self, base_url, token):
       self.base_url = base_url
       self.token = token

   def _get_headers(self):
       return {"Content-type": "application/json",
               "Authorization": f"Bearer {self.token}"}

   @allure.step("Поиск продукта по фразе: {phrase}")
   def search_product(self, phrase, customer_city_id = 54):
       params = {"customerCityId": customer_city_id,
                 "phrase": phrase}
       response = requests.get(self.base_url, headers=self._get_headers(), params=params)
       allure.attach(response.text, "Ответ API")
       return response