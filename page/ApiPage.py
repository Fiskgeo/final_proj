import requests
import allure

class ApiPage:

   def __init__(self, base_url, token):
       self.base_url = base_url
       self._token = token

   def _get_headers(self):
       return {"Content-type": "application/json"}