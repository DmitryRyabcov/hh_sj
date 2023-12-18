from api_work.abstract_api import AbstractVacanciesAPI
import requests
import os


class SuperJobAPI(AbstractVacanciesAPI):
    """
    Класс для получения вакансий с superjob.ru через API сайта
    """
    SJ_KEY = "v3.r.138038683.1f62df4fc1cdccb141804088967773ce2501adae.99cde644ae3c13be0c2c6fb72d4a14d1d7402e91"
    API_KEY = os.environ.get(SJ_KEY)

    def get_vacancies(self, text):
        headers = {"X-Api-App-Id": self.API_KEY}
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {"count": 1000, "page": 0, "keyword": text}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["objects"]